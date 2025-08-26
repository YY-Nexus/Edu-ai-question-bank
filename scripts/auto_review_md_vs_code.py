import re
import os
import difflib
import sys

md_files = [
    '../docs/系统UI设计方案文档.md',
    '../docs/教育AI全栈设计方案.md',
    '../docs/教育AI题库系统文档.md'
]
output_root = '../generated'
report_md = 'auto_review_report.md'
lang_ext = {
    'python': '.py',
    'javascript': '.js',
    'vue': '.vue',
    'yaml': '.yaml',
    'plaintext': '.txt',
    'mermaid': '.mmd',
    'json': '.json'
}

patterns = [
    r'[#]{1,3} ?文件名[:：] *([^\n]+)\n```(\w+)\n(.*?)```',
    r'[#]{1,3} ?([^\n]+)\n```(\w+)\n(.*?)```',
]

md_blocks = []
for md_path in md_files:
    if not os.path.isfile(md_path):
        continue
    with open(md_path, encoding='utf-8') as f:
        content = f.read()
    for pattern in patterns:
        for match in re.findall(pattern, content, re.DOTALL):
            filename, lang, code = match
            filename = filename.strip()
            filename = re.sub(r'^[# ]+', '', filename)
            filename = re.sub(r'[\\/:*?"<>|]', '_', filename)
            ext = lang_ext.get(lang.lower(), '.txt')
            if not filename.endswith(ext):
                filename += ext
            md_blocks.append({
                "filename": filename,
                "lang": lang,
                "code": code.strip()
            })

results = []
errors = []

for block in md_blocks:
    rel_path = block["filename"]
    abs_path = os.path.join(output_root, rel_path)
    md_code = block["code"]

    try:
        if os.path.isfile(abs_path):
            with open(abs_path, encoding='utf-8') as f:
                actual_code = f.read().strip()
            if actual_code == md_code:
                status = "✅ 完全一致"
            else:
                ratio = difflib.SequenceMatcher(None, md_code, actual_code).ratio()
                status = f"⚠️ 不一致（相似度 {ratio:.2f}）"
                errors.append(f"{rel_path} 内容不一致，相似度 {ratio:.2f}")
        else:
            status = "❌ 缺失"
            errors.append(f"{rel_path} 缺失")
    except Exception as e:
        status = f"❌ 读取失败: {e}"
        errors.append(f"{rel_path} 读取失败: {e}")

    results.append({
        "文件名": rel_path,
        "语言": block["lang"],
        "状态": status,
    })

with open(report_md, 'w', encoding='utf-8') as f:
    f.write("| 文件名 | 状态 | 语言 |\n|---|---|---|\n")
    for row in results:
        f.write(f"| {row['文件名']} | {row['状态']} | {row['语言']} |\n")

if errors:
    print("自动审核未通过：")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)
else:
    print("自动审核全部通过 ✅ ")
    sys.exit(0)