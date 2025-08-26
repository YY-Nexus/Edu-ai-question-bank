#!/usr/bin/env python3
"""
Auto Documentation Completion Engine
Automatically adds missing code files to documentation with descriptions and code blocks.
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from datetime import datetime

class AutoDocumentationEngine:
    def __init__(self, repo_root: str):
        self.repo_root = repo_root
        self.main_docs = {
            'docs/教育AI题库系统文档.md': 'system',
            'docs/教育AI全栈设计方案.md': 'design', 
            'docs/系统UI设计方案文档.md': 'ui'
        }
        
        # 文件分类到文档的映射
        self.file_to_doc_mapping = {
            'backend': 'docs/教育AI全栈设计方案.md',
            'frontend': 'docs/系统UI设计方案文档.md',
            'infrastructure': 'docs/教育AI题库系统文档.md',
            'scripts': 'docs/教育AI题库系统文档.md',
            'docs': None,  # 不自动添加文档文件到文档中
            'other': 'docs/教育AI题库系统文档.md'
        }

    def load_analysis_data(self) -> Tuple[Dict, Dict]:
        """加载分析数据"""
        inventory_file = os.path.join(self.repo_root, 'scripts', 'repo_inventory.json')
        analysis_file = os.path.join(self.repo_root, 'scripts', 'doc_analysis.json')
        
        with open(inventory_file, 'r', encoding='utf-8') as f:
            inventory = json.load(f)
        
        with open(analysis_file, 'r', encoding='utf-8') as f:
            analysis = json.load(f)
        
        return inventory, analysis

    def generate_file_description(self, file_info: Dict) -> str:
        """为文件生成中文描述"""
        category = file_info['category']
        file_type = file_info['type']
        file_path = file_info['path']
        
        # 基于文件路径和类型的描述模板
        descriptions = {
            'backend': {
                'yaml': 'Kubernetes后端服务部署配置文件，定义了后端应用的部署规范、服务配置和网络策略',
            },
            'frontend': {
                'yaml': 'Kubernetes前端服务部署配置文件，定义了前端应用的部署规范和负载均衡配置',
                'markdown': '前端UI系统设计文档，包含组件设计、样式规范和交互流程'
            },
            'infrastructure': {
                'yaml': 'Kubernetes基础设施配置文件，用于部署和管理容器化应用的基础组件',
                'python': '基础设施管理和自动化脚本，用于部署、配置和维护系统组件'
            },
            'scripts': {
                'python': '项目自动化脚本，用于代码生成、文档同步、部署和维护等任务',
                'bash': '系统运维Shell脚本，用于服务管理、数据库操作和系统维护',
                'sql': 'SQL数据库脚本，用于数据库结构优化、索引创建和数据维护',
                'markdown': '脚本使用说明和运行报告文档'
            },
            'other': {
                'yaml': 'CI/CD工作流配置文件，定义了自动化构建、测试和部署流程',
                'markdown': '项目相关的说明文档和报告文件'
            }
        }
        
        # 基于具体文件名的特殊描述
        special_descriptions = {
            'repo_scanner.py': '仓库文件扫描工具，用于分析项目结构和生成文件清单',
            'doc_parser.py': '文档解析工具，用于分析文档结构和识别文档化状态',
            'auto_review_md_vs_code.py': '文档代码一致性检查工具，对比文档中的代码块与实际文件',
            'sync_md_code.py': '文档代码同步工具，将文档中的代码块同步到实际文件',
            'rename_yaml_by_content.py': 'YAML文件重命名工具，根据文件内容自动分类和重命名',
            'ingress.yaml': 'Kubernetes Ingress配置，定义了外部访问路由和SSL终止',
            'redis-deployment.yaml': 'Redis缓存服务部署配置，用于会话存储和任务队列',
            'mariadb-configmap.yaml': 'MariaDB数据库配置映射，包含数据库初始化和配置参数',
            'auto-review.yml': 'GitHub Actions自动审查工作流，用于代码质量检查和文档同步验证'
        }
        
        # 获取文件名
        filename = Path(file_path).name
        
        # 检查特殊描述
        if filename in special_descriptions:
            return special_descriptions[filename]
        
        # 使用通用描述
        if category in descriptions and file_type in descriptions[category]:
            return descriptions[category][file_type]
        
        # 默认描述
        return f"{category}目录下的{file_type}文件，{filename}"

    def read_file_content(self, file_path: str) -> str:
        """安全读取文件内容"""
        abs_path = os.path.join(self.repo_root, file_path)
        try:
            with open(abs_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return content.strip()
        except UnicodeDecodeError:
            try:
                with open(abs_path, 'r', encoding='gb2312') as f:
                    content = f.read()
                return content.strip()
            except:
                return f"# 文件编码问题，无法读取: {file_path}"
        except Exception as e:
            return f"# 读取文件失败: {e}"

    def get_language_from_extension(self, file_path: str) -> str:
        """根据文件扩展名获取代码块语言"""
        ext_mapping = {
            '.py': 'python',
            '.js': 'javascript',
            '.vue': 'vue',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.json': 'json',
            '.md': 'markdown',
            '.sql': 'sql',
            '.sh': 'bash',
            '.txt': 'plaintext',
            '.mmd': 'mermaid'
        }
        
        ext = Path(file_path).suffix.lower()
        return ext_mapping.get(ext, 'plaintext')

    def generate_documentation_section(self, file_info: Dict) -> str:
        """为文件生成文档章节"""
        file_path = file_info['path']
        description = self.generate_file_description(file_info)
        content = self.read_file_content(file_path)
        language = self.get_language_from_extension(file_path)
        
        # 生成文档章节
        section = f"""

#### {file_path}

{description}

```{language}
{content}
```
"""
        return section

    def find_insertion_point(self, doc_content: str, category: str) -> int:
        """找到插入新章节的位置"""
        # 为不同类别的文件找到合适的插入位置
        insertion_patterns = {
            'infrastructure': [
                r'## 4\. 部署文档',
                r'### 4\.2 生产环境部署',
                r'## 部署',
                r'## k8s',
                r'## Kubernetes'
            ],
            'scripts': [
                r'## 脚本',
                r'## 工具',
                r'## 自动化',
                r'## 维护',
                r'$'  # 文档末尾
            ],
            'backend': [
                r'## 后端',
                r'## backend',
                r'## 核心文件实现',
                r'### 1\. 后端核心文件'
            ],
            'frontend': [
                r'## 前端',
                r'## frontend',
                r'## UI',
                r'## 组件'
            ],
            'other': [
                r'## 其他',
                r'## 配置',
                r'$'  # 文档末尾
            ]
        }
        
        patterns = insertion_patterns.get(category, [r'$'])
        
        for pattern in patterns:
            if pattern == '$':
                return len(doc_content)
            
            match = re.search(pattern, doc_content, re.MULTILINE)
            if match:
                # 找到下一个同级或更高级标题的位置
                section_start = match.start()
                remaining_content = doc_content[section_start:]
                
                # 查找下一个同级标题
                next_section = re.search(r'\n## ', remaining_content)
                if next_section:
                    return section_start + next_section.start()
                else:
                    return len(doc_content)
        
        # 如果没有找到合适的位置，插入到末尾
        return len(doc_content)

    def add_section_header_if_needed(self, doc_content: str, category: str) -> str:
        """如果需要，添加新的章节标题"""
        section_headers = {
            'infrastructure': '## 基础设施配置文件',
            'scripts': '## 自动化脚本和工具',
            'other': '## 其他配置文件'
        }
        
        header = section_headers.get(category)
        if not header:
            return doc_content
        
        # 检查是否已存在相应的章节
        if re.search(header.replace('##', r'##\s*'), doc_content):
            return doc_content
        
        # 在合适的位置添加章节标题
        insertion_point = self.find_insertion_point(doc_content, category)
        
        new_section = f"\n\n{header}\n"
        new_content = (doc_content[:insertion_point] + 
                      new_section + 
                      doc_content[insertion_point:])
        
        return new_content

    def update_documentation(self, undocumented_files: List[Dict]) -> Dict:
        """更新文档，添加未文档化的文件"""
        updates = {}
        
        # 按文档分组文件
        files_by_doc = {}
        for file_info in undocumented_files:
            category = file_info['category']
            target_doc = self.file_to_doc_mapping.get(category)
            
            if target_doc and target_doc in self.main_docs:
                if target_doc not in files_by_doc:
                    files_by_doc[target_doc] = []
                files_by_doc[target_doc].append(file_info)
        
        # 更新每个文档
        for doc_path, files in files_by_doc.items():
            abs_doc_path = os.path.join(self.repo_root, doc_path)
            
            if not os.path.exists(abs_doc_path):
                print(f"⚠️ 文档文件不存在: {doc_path}")
                continue
            
            # 读取原始文档
            with open(abs_doc_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            updated_content = original_content
            
            # 按类别分组文件
            files_by_category = {}
            for file_info in files:
                category = file_info['category']
                if category not in files_by_category:
                    files_by_category[category] = []
                files_by_category[category].append(file_info)
            
            # 为每个类别添加文件
            for category, category_files in files_by_category.items():
                # 添加章节标题（如果需要）
                updated_content = self.add_section_header_if_needed(updated_content, category)
                
                # 为每个文件生成文档章节
                for file_info in category_files:
                    section = self.generate_documentation_section(file_info)
                    
                    # 找到插入位置
                    insertion_point = self.find_insertion_point(updated_content, category)
                    
                    # 插入新章节
                    updated_content = (updated_content[:insertion_point] + 
                                     section + 
                                     updated_content[insertion_point:])
            
            # 保存更新的文档
            backup_path = abs_doc_path + f'.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
            
            # 创建备份
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            # 保存更新
            with open(abs_doc_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            updates[doc_path] = {
                'files_added': len(files),
                'backup_created': backup_path,
                'categories': list(files_by_category.keys())
            }
            
            print(f"✅ 已更新文档: {doc_path}")
            print(f"   添加文件: {len(files)} 个")
            print(f"   备份创建: {backup_path}")
        
        return updates

def main():
    """主函数"""
    repo_root = '/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank'
    
    # 初始化引擎
    engine = AutoDocumentationEngine(repo_root)
    
    # 加载分析数据
    try:
        inventory, analysis = engine.load_analysis_data()
    except FileNotFoundError as e:
        print(f"❌ 请先运行 repo_scanner.py 和 doc_parser.py: {e}")
        return
    
    # 获取未文档化的文件
    undocumented_files = []
    existing_files = {f['path']: f for f in inventory['files']}
    
    for file_path in analysis['comparison']['existing_but_undocumented']:
        if file_path in existing_files:
            undocumented_files.append(existing_files[file_path])
    
    # 过滤掉不需要自动文档化的文件（如文档文件本身）
    filtered_files = [
        f for f in undocumented_files 
        if f['category'] != 'docs' and not f['path'].endswith('.md')
    ]
    
    print(f"🚀 开始自动补全文档...")
    print(f"📊 将处理 {len(filtered_files)} 个未文档化的文件")
    
    # 按类别显示文件
    categories = {}
    for f in filtered_files:
        cat = f['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(f['path'])
    
    for category, files in categories.items():
        print(f"  [{category}] {len(files)} 个文件")
    
    # 执行文档更新
    updates = engine.update_documentation(filtered_files)
    
    print(f"\n✅ 文档自动补全完成!")
    print(f"📝 更新了 {len(updates)} 个文档文件:")
    
    for doc_path, info in updates.items():
        print(f"  {doc_path}: 添加了 {info['files_added']} 个文件")
    
    # 保存更新报告
    report_file = os.path.join(repo_root, 'scripts', 'auto_completion_report.json')
    report = {
        'timestamp': datetime.now().isoformat(),
        'processed_files': len(filtered_files),
        'updated_docs': updates,
        'files_by_category': categories
    }
    
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n📄 更新报告已保存到: {report_file}")

if __name__ == "__main__":
    main()