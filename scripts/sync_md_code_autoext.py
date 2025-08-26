import re
import os

md_path = 'docs/教育AI题库系统文档.md'
project_root = '.'  # 项目根目录

# 代码块语言到扩展名映射
lang_ext = {
    'python': '.py',
    'javascript': '.js',
    'js': '.js',
    'vue': '.vue',
    'yaml': '.yaml',
    'yml': '.yml',
    'bash': '.sh',
    'plaintext': '.txt',
    'mermaid': '.mmd',
    'sql': '.sql',
    'markdown': '.md',
}

# 支持常见代码块前缀格式
patterns = [
    r'####\s*([^\n]+)\n```(\w+)\n(.*?)```',
    r'文件名[:：] *([^\n]+)\n```(\w+)\n(.*?)```',
    r'#\s*([^\n]+)\n```(\w+)\n(.*?)```',
]

with open(md_path, encoding='utf-8') as f:
    md_content = f.read()

blocks = []
for pattern in patterns:
    for match in re.findall(pattern, md_content, re.DOTALL):
        filename, lang, code = match
        filename = filename.strip()
        lang = lang.strip().lower()
        code = code.strip()
        # 自动补充扩展名
        ext = lang_ext.get(lang, '.txt')
        if not filename.endswith(ext):
            filename += ext
        blocks.append({
            "filename": filename,
            "lang": lang,
            "code": code
        })

for block in blocks:
    rel_path = block["filename"]
    abs_path = os.path.join(project_root, rel_path)
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    with open(abs_path, 'w', encoding='utf-8') as f:
        f.write(block["code"] + '\n')
    print(f'已保存: {abs_path}')