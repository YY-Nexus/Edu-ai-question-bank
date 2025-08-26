#!/usr/bin/env python3
"""
Repository Scanner for Auto Documentation Completion
Scans the repository for all code files and generates an inventory.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
import json

# 文件类型映射
FILE_TYPES = {
    '.py': 'python',
    '.js': 'javascript', 
    '.vue': 'vue',
    '.yaml': 'yaml',
    '.yml': 'yaml',
    '.json': 'json',
    '.md': 'markdown',
    '.sql': 'sql',
    '.sh': 'bash',
    '.dockerfile': 'dockerfile',
    '.txt': 'plaintext',
    '.mmd': 'mermaid'
}

# 目录分类
DIRECTORY_CATEGORIES = {
    'backend': ['backend', 'server', 'api'],
    'frontend': ['frontend', 'client', 'web', 'ui'],
    'infrastructure': ['k8s', 'kubernetes', 'infra', 'deploy', 'docker'],
    'scripts': ['scripts', 'tools', 'utils'],
    'docs': ['docs', 'documentation'],
    'config': ['config', 'conf', 'settings']
}

def get_file_category(file_path: str) -> str:
    """根据文件路径确定文件类别"""
    path_parts = Path(file_path).parts
    
    for category, keywords in DIRECTORY_CATEGORIES.items():
        for part in path_parts:
            if any(keyword in part.lower() for keyword in keywords):
                return category
    
    return 'other'

def get_file_type(file_path: str) -> str:
    """根据文件扩展名确定文件类型"""
    ext = Path(file_path).suffix.lower()
    return FILE_TYPES.get(ext, 'unknown')

def scan_repository(repo_root: str) -> Dict:
    """扫描仓库中的所有代码文件"""
    repo_path = Path(repo_root)
    file_inventory = {
        'summary': {
            'total_files': 0,
            'categories': {},
            'file_types': {}
        },
        'files': []
    }
    
    # 忽略的目录和文件
    ignore_patterns = {
        '.git', '__pycache__', 'node_modules', '.DS_Store', 
        '*.pyc', '*.log', '.vscode', '.idea'
    }
    
    for root, dirs, files in os.walk(repo_path):
        # 过滤忽略的目录
        dirs[:] = [d for d in dirs if d not in ignore_patterns]
        
        for file in files:
            # 跳过隐藏文件和忽略的文件
            if file.startswith('.') and file not in ['.gitignore', '.env.example']:
                continue
                
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, repo_root)
            
            # 跳过忽略的文件模式
            if any(pattern in file for pattern in ignore_patterns):
                continue
            
            file_type = get_file_type(file_path)
            if file_type == 'unknown':
                continue
                
            category = get_file_category(relative_path)
            
            file_info = {
                'path': relative_path,
                'absolute_path': file_path,
                'category': category,
                'type': file_type,
                'size': os.path.getsize(file_path),
                'is_documented': False  # 后续会更新
            }
            
            file_inventory['files'].append(file_info)
            
            # 更新统计信息
            file_inventory['summary']['total_files'] += 1
            file_inventory['summary']['categories'][category] = \
                file_inventory['summary']['categories'].get(category, 0) + 1
            file_inventory['summary']['file_types'][file_type] = \
                file_inventory['summary']['file_types'].get(file_type, 0) + 1
    
    return file_inventory

def read_file_content(file_path: str) -> str:
    """安全读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='gb2312') as f:
                return f.read()
        except:
            return f"# 无法读取文件内容 (编码问题): {file_path}"
    except Exception as e:
        return f"# 读取文件失败: {e}"

def generate_file_description(file_info: Dict) -> str:
    """为文件生成描述"""
    category = file_info['category']
    file_type = file_info['type']
    path = file_info['path']
    
    descriptions = {
        'backend': {
            'python': '后端Python源码文件',
            'yaml': '后端部署配置文件',
            'json': '后端配置文件'
        },
        'frontend': {
            'javascript': '前端JavaScript文件',
            'vue': '前端Vue组件文件',
            'json': '前端配置文件'
        },
        'infrastructure': {
            'yaml': 'Kubernetes部署配置文件',
            'python': '基础设施管理脚本'
        },
        'scripts': {
            'python': '自动化脚本文件',
            'bash': 'Shell脚本文件'
        },
        'docs': {
            'markdown': '项目文档文件'
        }
    }
    
    if category in descriptions and file_type in descriptions[category]:
        return descriptions[category][file_type]
    
    return f"{category}目录下的{file_type}文件"

def main():
    """主函数"""
    repo_root = '/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank'
    
    print("🔍 正在扫描仓库文件...")
    inventory = scan_repository(repo_root)
    
    print(f"\n📊 扫描结果统计:")
    print(f"总文件数: {inventory['summary']['total_files']}")
    
    print(f"\n📁 按类别分布:")
    for category, count in inventory['summary']['categories'].items():
        print(f"  {category}: {count} 个文件")
    
    print(f"\n📄 按文件类型分布:")
    for file_type, count in inventory['summary']['file_types'].items():
        print(f"  {file_type}: {count} 个文件")
    
    print(f"\n📋 详细文件清单:")
    for file_info in sorted(inventory['files'], key=lambda x: (x['category'], x['path'])):
        print(f"  [{file_info['category']}] {file_info['path']} ({file_info['type']})")
    
    # 保存扫描结果
    output_file = os.path.join(repo_root, 'scripts', 'repo_inventory.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 扫描结果已保存到: {output_file}")
    
    return inventory

if __name__ == "__main__":
    main()