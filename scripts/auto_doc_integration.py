#!/usr/bin/env python3
"""
Auto Documentation Completion - Integration Script
完整的自动文档补全流程，包括扫描、分析和更新
"""

import os
import sys
import json
from datetime import datetime

def run_command(command, description):
    """运行命令并显示进度"""
    print(f"🔄 {description}...")
    result = os.system(command)
    if result == 0:
        print(f"✅ {description} - 完成")
        return True
    else:
        print(f"❌ {description} - 失败")
        return False

def main():
    """主流程"""
    print("🚀 教育AI题库系统 - 自动文档补全系统")
    print("=" * 50)
    
    repo_root = '/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank'
    os.chdir(repo_root)
    
    # 步骤1：扫描仓库文件
    if not run_command("python scripts/repo_scanner.py", "扫描仓库文件结构"):
        sys.exit(1)
    
    # 步骤2：分析文档状态
    if not run_command("python scripts/doc_parser.py", "分析文档化状态"):
        sys.exit(1)
    
    # 步骤3：自动补全文档
    if not run_command("python scripts/auto_doc_completion.py", "执行文档自动补全"):
        sys.exit(1)
    
    # 步骤4：验证结果
    print("\n🔍 验证补全结果...")
    if not run_command("python scripts/doc_parser.py > /tmp/final_status.txt", "重新分析文档状态"):
        sys.exit(1)
    
    # 显示最终统计
    print("\n📊 补全结果统计:")
    
    try:
        with open('scripts/auto_completion_report.json', 'r', encoding='utf-8') as f:
            report = json.load(f)
        
        print(f"  处理时间: {report['timestamp']}")
        print(f"  处理文件数: {report['processed_files']}")
        print(f"  更新文档数: {len(report['updated_docs'])}")
        
        print(f"\n📝 更新的文档:")
        for doc_path, info in report['updated_docs'].items():
            print(f"  - {doc_path}: +{info['files_added']} 个文件")
        
        print(f"\n📁 按类别分布:")
        for category, files in report['files_by_category'].items():
            print(f"  - {category}: {len(files)} 个文件")
    
    except Exception as e:
        print(f"⚠️ 无法读取补全报告: {e}")
    
    print("\n✅ 自动文档补全流程完成!")
    print("\n📋 下一步建议:")
    print("1. 检查更新后的文档内容是否准确")
    print("2. 提交更改作为 Pull Request")
    print("3. 团队审核文档补全结果")
    print("4. 考虑添加更多详细说明和使用示例")
    
    return True

if __name__ == "__main__":
    main()