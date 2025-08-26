import re
import os
import difflib
import csv

md_path = '../docs/教育AI题库系统文档.md'
project_root = '../'
report_md = 'code_progress_report.md'
report_csv = 'code_progress_report.csv'

# 支持多种标记格式
patterns = [
    r'# 文件名[:：] *([^\n]+)\n```(\w+)\n(.*?)```',
    r'## *([^\n]+)\n```(\w+)\n(.*?)```',
    r'文件名[:：] *([^\n]+)\n```(\w+)\n(.*?)```',
    r'### *([^\n]+)\n```(\w+)\n(.*?)```',
    r'#### *([^\n]+)\n```(\w+)\n(.*?)```',
]

md_blocks = []
with open(md_path, encoding='utf-8') as f:
    md_content = f.read()
for pattern in patterns:
    for match in re.findall(pattern, md_content, re.DOTALL):
        filename, lang, code = match
        md_blocks.append({
            "filename": filename.strip(),
            "lang": lang,
            "code": code.strip()
        })

results = []
for block in md_blocks:
    rel_path = block["filename"]
    abs_path = os.path.join(project_root, rel_path)
    status = ""
    detail = ""
    md_code = block["code"]

    need_fix = False
    if os.path.isfile(abs_path):
        with open(abs_path, encoding='utf-8') as f:
            actual_code = f.read().strip()
        if actual_code == md_code:
            status = "✅ 完全一致"
            detail = ""
        else:
            ratio = difflib.SequenceMatcher(None, md_code, actual_code).ratio()
            status = f"⚠️ 不一致（已自动修复，相似度 {ratio:.2f}）"
            diff = '\n'.join(list(difflib.unified_diff(md_code.splitlines(), actual_code.splitlines(), lineterm='', n=3)))
            detail = diff[:200] + "..." if len(diff) > 200 else diff
            need_fix = True
    else:
        status = "❌ 缺失（已自动修复）"
        detail = ""
        need_fix = True

    # 自动修复
    if need_fix:
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(md_code + '\n')

    results.append({
        "文件名": rel_path,
        "语言": block["lang"],
        "状态": status,
        "相似度/差异": detail
    })

# 生成 Markdown 报表
with open(report_md, 'w', encoding='utf-8') as f:
    f.write("| 文件名 | 状态 | 语言 | 相似度/差异 |\n")
    f.write("|---|---|---|---|\n")
    for row in results:
        f.write(f"| {row['文件名']} | {row['状态']} | {row['语言']} | {row['相似度/差异'].replace('|', '\\|')[:100]} |\n")

# 生成 CSV 报表
with open(report_csv, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["文件名", "状态", "语言", "相似度/差异"])
    for row in results:
        writer.writerow([row['文件名'], row['状态'], row['语言'], row['相似度/差异'][:100]])

print(f"已生成进度报表：{report_md} 和 {report_csv}")
print("所有不一致或缺失文件已自动修复。")