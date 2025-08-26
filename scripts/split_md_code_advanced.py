import re
import os

md_path = '../docs/教育AI题库系统文档.md'
output_root = '../'

with open(md_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 支持 "#### backend/main.py" 或 "#### frontend/src/api/index.js" 这种格式
pattern = r'####\s*([^\n]+)\n```(\w+)\n(.*?)```'
matches = re.findall(pattern, content, re.DOTALL)

for filename, lang, code in matches:
    file_path = os.path.join(output_root, filename.strip())
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(code.strip() + '\n')
    print(f'已保存: {file_path}')