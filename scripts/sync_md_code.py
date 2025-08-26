import re
import os

md_path = '../docs/教育AI题库系统文档.md'
project_root = '.'  # 当前项目根目录

# 支持常见代码块前缀格式
patterns = [
    r'####\s*([^\n]+)\n```(\w+)\n(.*?)```',
    r'文件名[:：] *([^\n]+)\n```(\w+)\n(.*?)```',
]

with open(md_path, encoding='utf-8') as f:
    md_content = f.read()

blocks = []
for pattern in patterns:
    for match in re.findall(pattern, md_content, re.DOTALL):
        filename, lang, code = match
        blocks.append({
            "filename": filename.strip(),
            "lang": lang,
            "code": code.strip()
        })

for block in blocks:
    rel_path = block["filename"]
    abs_path = os.path.join(project_root, rel_path)
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    with open(abs_path, 'w', encoding='utf-8') as f:
        f.write(block["code"] + '\n')
    print(f'已覆盖保存: {abs_path}')