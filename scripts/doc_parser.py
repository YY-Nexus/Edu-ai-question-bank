#!/usr/bin/env python3
"""
Documentation Parser for Auto Documentation Completion
Parses existing documentation to identify documented vs missing code files.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple

class DocumentationParser:
    def __init__(self, repo_root: str):
        self.repo_root = repo_root
        self.doc_files = [
            'docs/教育AI题库系统文档.md',
            'docs/教育AI全栈设计方案.md', 
            'docs/系统UI设计方案文档.md'
        ]
        
        # 匹配代码块的正则模式
        self.code_block_patterns = [
            r'####\s*([^\n]+)\n```(\w+)\n(.*?)```',  # #### filename
            r'###\s*([^\n]+)\n```(\w+)\n(.*?)```',   # ### filename
            r'##\s*([^\n]+)\n```(\w+)\n(.*?)```',    # ## filename
            r'文件名[:：]\s*([^\n]+)\n```(\w+)\n(.*?)```',  # 文件名: filename
            r'[#]*\s*([^\n]*\.(?:py|js|vue|yaml|yml|json|md|sql|sh))\s*\n```(\w+)\n(.*?)```'  # 文件扩展名
        ]
        
        # 路径引用模式
        self.path_reference_patterns = [
            r'(?:backend|frontend|k8s|scripts|docs)/[^\s\)]+\.(?:py|js|vue|yaml|yml|json|md|sql|sh)',
            r'[^\s\)]+/[^\s\)]+\.(?:py|js|vue|yaml|yml|json|md|sql|sh)'
        ]

    def parse_documentation(self) -> Dict:
        """解析文档，提取所有代码引用和代码块"""
        result = {
            'documented_files': {},  # 文件路径 -> 文档信息
            'code_blocks': [],       # 代码块列表
            'file_references': set(), # 文件路径引用
            'missing_files': set(),   # 文档中引用但不存在的文件
            'doc_summary': {}         # 每个文档的摘要
        }
        
        for doc_file in self.doc_files:
            doc_path = os.path.join(self.repo_root, doc_file)
            if not os.path.exists(doc_path):
                continue
                
            print(f"📖 解析文档: {doc_file}")
            
            with open(doc_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 解析代码块
            code_blocks = self._extract_code_blocks(content, doc_file)
            result['code_blocks'].extend(code_blocks)
            
            # 解析文件路径引用
            file_refs = self._extract_file_references(content)
            result['file_references'].update(file_refs)
            
            # 文档摘要
            result['doc_summary'][doc_file] = {
                'code_blocks': len(code_blocks),
                'file_references': len(file_refs),
                'size': len(content)
            }
        
        # 处理文档化的文件
        for block in result['code_blocks']:
            if block['filename']:
                result['documented_files'][block['filename']] = {
                    'source_doc': block['source_doc'],
                    'language': block['language'],
                    'has_code': bool(block['code'].strip()),
                    'code_length': len(block['code'])
                }
        
        return result

    def _extract_code_blocks(self, content: str, source_doc: str) -> List[Dict]:
        """从内容中提取代码块"""
        code_blocks = []
        
        for pattern in self.code_block_patterns:
            matches = re.findall(pattern, content, re.DOTALL)
            for match in matches:
                if len(match) == 3:
                    filename, language, code = match
                else:
                    continue
                    
                # 清理文件名
                filename = self._clean_filename(filename)
                
                if filename:
                    code_blocks.append({
                        'filename': filename,
                        'language': language.lower(),
                        'code': code.strip(),
                        'source_doc': source_doc
                    })
        
        return code_blocks

    def _extract_file_references(self, content: str) -> Set[str]:
        """从内容中提取文件路径引用"""
        file_refs = set()
        
        for pattern in self.path_reference_patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                cleaned_path = self._clean_path_reference(match)
                if cleaned_path:
                    file_refs.add(cleaned_path)
        
        return file_refs

    def _clean_filename(self, filename: str) -> str:
        """清理文件名"""
        # 移除前导的 # 符号和空格
        filename = re.sub(r'^[#\s]+', '', filename.strip())
        
        # 移除 "文件名:" 前缀
        filename = re.sub(r'^文件名[:：]\s*', '', filename)
        
        # 移除特殊字符（但保留路径分隔符）
        filename = re.sub(r'[^\w\-_./\\]', '', filename)
        
        # 标准化路径分隔符
        filename = filename.replace('\\', '/')
        
        # 移除多余的路径分隔符
        filename = re.sub(r'/+', '/', filename)
        
        return filename if filename else None

    def _clean_path_reference(self, path: str) -> str:
        """清理路径引用"""
        # 移除周围的标点符号
        path = re.sub(r'^[^\w/]+|[^\w/]+$', '', path)
        
        # 标准化路径分隔符
        path = path.replace('\\', '/')
        
        return path if path else None

    def compare_with_actual_files(self, inventory: Dict) -> Dict:
        """比较文档化的文件与实际存在的文件"""
        doc_result = self.parse_documentation()
        
        actual_files = {f['path'] for f in inventory['files']}
        documented_files = set(doc_result['documented_files'].keys())
        all_referenced_files = documented_files | doc_result['file_references']
        
        comparison = {
            'existing_but_undocumented': actual_files - all_referenced_files,
            'documented_but_missing': all_referenced_files - actual_files,
            'documented_and_existing': actual_files & documented_files,
            'only_referenced': doc_result['file_references'] - documented_files,
            'statistics': {
                'total_actual_files': len(actual_files),
                'total_documented_files': len(documented_files),
                'total_referenced_files': len(doc_result['file_references']),
                'undocumented_count': len(actual_files - all_referenced_files),
                'missing_count': len(all_referenced_files - actual_files)
            }
        }
        
        return comparison, doc_result

def main():
    """主函数"""
    repo_root = '/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank'
    
    # 加载仓库扫描结果
    inventory_file = os.path.join(repo_root, 'scripts', 'repo_inventory.json')
    if not os.path.exists(inventory_file):
        print("❌ 请先运行 repo_scanner.py 生成文件清单")
        return
    
    with open(inventory_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)
    
    # 解析文档
    parser = DocumentationParser(repo_root)
    comparison, doc_result = parser.compare_with_actual_files(inventory)
    
    print("📚 文档解析完成\n")
    
    print("📊 统计信息:")
    stats = comparison['statistics']
    print(f"  实际文件数: {stats['total_actual_files']}")
    print(f"  文档化文件数: {stats['total_documented_files']}")
    print(f"  引用文件数: {stats['total_referenced_files']}")
    print(f"  未文档化文件数: {stats['undocumented_count']}")
    print(f"  缺失文件数: {stats['missing_count']}")
    
    print(f"\n📝 文档摘要:")
    for doc, summary in doc_result['doc_summary'].items():
        print(f"  {doc}:")
        print(f"    代码块: {summary['code_blocks']} 个")
        print(f"    文件引用: {summary['file_references']} 个")
    
    print(f"\n🆕 存在但未文档化的文件 ({len(comparison['existing_but_undocumented'])}):")
    for file_path in sorted(comparison['existing_but_undocumented']):
        print(f"  - {file_path}")
    
    print(f"\n❌ 文档化但缺失的文件 ({len(comparison['documented_but_missing'])}):")
    for file_path in sorted(comparison['documented_but_missing']):
        print(f"  - {file_path}")
    
    print(f"\n✅ 文档化且存在的文件 ({len(comparison['documented_and_existing'])}):")
    for file_path in sorted(comparison['documented_and_existing']):
        print(f"  - {file_path}")
    
    # 保存分析结果
    output_file = os.path.join(repo_root, 'scripts', 'doc_analysis.json')
    analysis_result = {
        'comparison': comparison,
        'documentation_result': doc_result
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis_result, f, ensure_ascii=False, indent=2, default=list)
    
    print(f"\n💾 分析结果已保存到: {output_file}")
    
    return analysis_result

if __name__ == "__main__":
    main()