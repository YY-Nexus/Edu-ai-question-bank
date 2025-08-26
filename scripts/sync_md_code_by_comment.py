
**正确的自动拆分脚本如下：**  
它会自动识别代码块语言和首行文件名注释，将代码保存到对应文件（自动补充扩展名）。

````python
import re
import os

md_path = '../docs/教育AI题库系统文档.md'
project_root = '..'

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

with open(md_path, encoding='utf-8') as f:
    md_content = f.read()

# 匹配代码块，提取语言和内容
pattern = r'```(\w+)\n(.*?)(?=```)'  # 只匹配代码块
matches = re.findall(pattern, md_content, re.DOTALL)

for lang, code in matches:
    lang = lang.strip().lower()
    code_lines = code.strip().splitlines()
    if not code_lines:
        continue
    # 文件名在首行注释，如 "# backend/database.py"
    first_line = code_lines[0].strip()
    file_match = re.match(r'#\s*([\w\-/\.]+)', first_line)
    if file_match:
        filename = file_match.group(1)
        ext = lang_ext.get(lang, '.txt')
        if not filename.endswith(ext):
            filename += ext
        abs_path = os.path.join(project_root, filename)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        # 去掉首行文件名注释
        code_to_write = '\n'.join(code_lines[1:]).strip() + '\n'
        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(code_to_write)
        print(f'已保存: {abs_path}')