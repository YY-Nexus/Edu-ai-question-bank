import re
import os

md_files = [
    '../docs/系统UI设计方案文档.md',
    '../docs/教育AI全栈设计方案.md',
    '../docs/教育AI题库系统文档.md'
]
project_root = '../'

lang_ext = {
    'python': '.py',
    'javascript': '.js',
    'vue': '.vue',
    'yaml': '.yaml',
    'plaintext': '.txt',
    'mermaid': '.mmd',
    'json': '.json'
}

def auto_dir(filename):
    # 只要是带目录的文件名，直接拼接到 project_root
    if '/' in filename or filename.endswith(('.yml', '.yaml')):
        return os.path.join(project_root, filename)
    else:
        return os.path.join(project_root, 'misc', filename)

patterns = [
    r'[#]{1,3} ?文件名[:：] *([^\n]+)\n```(\w+)\n(.*?)```',
    r'[#]{1,3} ?([^\n]+)\n```(\w+)\n(.*?)```',
]

generated_files = []

for md_path in md_files:
    if not os.path.isfile(md_path):
        print(f"未找到文档: {md_path}")
        continue
    with open(md_path, encoding='utf-8') as f:
        content = f.read()

    found = {}
    for pattern in patterns:
        for match in re.findall(pattern, content, re.DOTALL):
            filename, lang, code = match
            filename = re.sub(r'^[# ]+', '', filename.strip())
            # 只过滤非法字符，不替换 /
            filename = re.sub(r'[:*?"<>|]', '_', filename)
            ext = lang_ext.get(lang.lower(), '.txt')
            if not filename.endswith(ext):
                filename += ext
            path = auto_dir(filename)
            if path not in found:
                found[path] = []
            found[path].append(code.strip())

    for path, codes in found.items():
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(codes))
        print(f'已保存: {path}，包含 {len(codes)} 段代码')
        generated_files.append(os.path.relpath(path, project_root))

# 自动生成文件树
def print_tree(paths):
    tree = {}
    for p in paths:
        parts = p.split(os.sep)
        cur = tree
        for part in parts:
            cur = cur.setdefault(part, {})
    def _print(cur, prefix=''):
        for k, v in cur.items():
            print(prefix + '├── ' + k)
            _print(v, prefix + '│   ')
    print("\n生成文件树：")
    _print(tree, '')

print_tree(generated_files)