#!/usr/bin/env python3
"""社交媒体内容解析器

解析朋友圈、微博、小红书、Instagram 等社交媒体截图或导出文件。
图片内容由当前 Agent 主机提供的文件/图片读取能力处理；本工具只扫描本地
目录并处理文本导出，不依赖特定 Agent 或工具名称。

Usage:
    python3 social_parser.py --dir <screenshot_dir> --output <output_path>
"""

import argparse
import os
import sys
from pathlib import Path


def scan_directory(dir_path: str) -> dict:
    """扫描目录，按类型分类文件"""
    files = {'images': [], 'texts': [], 'other': []}
    
    image_exts = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'}
    text_exts = {'.txt', '.md', '.json', '.csv'}
    
    for root, dirs, filenames in os.walk(dir_path):
        for fname in filenames:
            fpath = os.path.join(root, fname)
            ext = Path(fname).suffix.lower()
            if ext in image_exts:
                files['images'].append(fpath)
            elif ext in text_exts:
                files['texts'].append(fpath)
            else:
                files['other'].append(fpath)
    
    return files


def main():
    parser = argparse.ArgumentParser(description='社交媒体内容解析器')
    parser.add_argument('--dir', required=True, help='截图/文件目录')
    parser.add_argument('--output', required=True, help='输出文件路径')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.dir):
        print(f"错误：目录不存在 {args.dir}", file=sys.stderr)
        sys.exit(1)
    
    files = scan_directory(args.dir)
    
    os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write("# 社交媒体内容扫描结果\n\n")
        f.write(f"扫描目录：{args.dir}\n\n")
        
        f.write(f"## 文件统计\n")
        f.write(f"- 图片文件：{len(files['images'])} 个\n")
        f.write(f"- 文本文件：{len(files['texts'])} 个\n")
        f.write(f"- 其他文件：{len(files['other'])} 个\n\n")
        
        if files['images']:
            f.write("## 图片列表（请用当前 Agent 主机的图片读取能力逐一查看）\n")
            for img in sorted(files['images']):
                f.write(f"- {img}\n")
            f.write("\n")
        
        if files['texts']:
            f.write("## 文本内容\n")
            for txt in sorted(files['texts']):
                f.write(f"\n### {os.path.basename(txt)}\n")
                try:
                    with open(txt, 'r', encoding='utf-8', errors='ignore') as tf:
                        content = tf.read(5000)
                    f.write(f"```\n{content}\n```\n")
                except Exception as e:
                    f.write(f"读取失败：{e}\n")
    
    print(f"扫描完成，结果已写入 {args.output}")
    print("提示：图片截图需使用当前 Agent 主机的图片读取能力查看，本工具仅列出文件路径")


if __name__ == '__main__':
    main()
