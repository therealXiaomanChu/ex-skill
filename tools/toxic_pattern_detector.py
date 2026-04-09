#!/usr/bin/env python3
"""
有毒对话模式检测器

检测聊天记录中的 PUA 话术、煤气灯操纵、情感操控等有毒行为模式。
Inspired by: "同事甩锅 vs 前任甩锅"

用法:
    python3 toxic_pattern_detector.py --input <chat_file> --output <report_file>
"""

import argparse
import json
import re
from collections import defaultdict
from typing import Dict, List, Tuple


# PUA/煤气灯话术模式库
TOXIC_PATTERNS = {
    "gaslighting": {
        "name": "煤气灯操纵",
        "description": "让对方质疑自己的记忆、感知或理智",
        "patterns": [
            r"你想太多了",
            r"你太敏感了",
            r"我从来没说过",
            r"你记错了",
            r"我不是那个意思",
            r"你非要这么想我也没办法",
            r"你能不能别无理取闹",
            r"这都是你想象出来的",
            r"你太作了",
            r"正常人都不会这么想",
            r"你是不是有病",
            r"你心理有问题吧",
        ]
    },
    "blame_shifting": {
        "name": "甩锅",
        "description": "把责任推给对方或外部因素",
        "patterns": [
            r"都是因为你",
            r"要不是你",
            r"我这样都是你逼的",
            r"你以为我想吗",
            r"这个需求改了好几个地方",
            r"上线时间对上了吗",
            r"还有其他变更",
            r"是你先",
            r"明明是你",
            r"我没义务",
            r"这不是我的问题",
        ]
    },
    "emotional_manipulation": {
        "name": "情感操控",
        "description": "利用对方的感情进行操控",
        "patterns": [
            r"你要是真的爱我就",
            r"我为你付出了这么多",
            r"你看看别人家的",
            r"算了不说了",
            r"随便你",
            r"你开心就好",
            r"我都行",
            r"无所谓",
            r"反正也没人在乎我",
            r"我这样的人",
            r"你不配",
            r"除了我谁还会要你",
        ]
    },
    "silent_treatment": {
        "name": "冷暴力",
        "description": "用沉默/疏远作为惩罚",
        "patterns": [
            r"嗯",
            r"哦",
            r"行",
            r"好",
            r"在忙",
            r"晚点说",
            r"不想说",
            r"没什么好说的",
            r"你非要这样想",
            r"我累了",
            r"睡了",
        ]
    },
    "negging": {
        "name": "打压 (Negging)",
        "description": "通过轻微贬低来降低对方自信",
        "patterns": [
            r"你这个都不懂",
            r"这么简单",
            r"我随便说说你都当真",
            r"你这样很",
            r"说实话你不适合",
            r"你太天真了",
            r"你太幼稚了",
            r"你太情绪化了",
            r"你这样找不到对象的",
            r"我这是为你好",
        ]
    },
    "love_bombing": {
        "name": "爱意轰炸",
        "description": "过度的甜言蜜语后突然冷淡（操控周期）",
        "patterns": [
            r"你是我的唯一",
            r"没有你我活不下去",
            r"我从来没有这么爱过一个人",
            r"你就是我的灵魂伴侣",
            r"我们永远不分开",
            r"我保证",
            r"我发誓",
            r"这次真的不一样",
            r"我会改的",
            r"再给我一次机会",
        ]
    }
}


def load_chat_data(input_file: str) -> List[Dict]:
    """加载聊天记录"""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 尝试 JSON 格式
    if content.strip().startswith('['):
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            pass
    
    # 简单文本格式解析 (假设格式：[时间] 发送者：内容)
    messages = []
    pattern = r'\[([^\]]+)\]\s*(\w+)[:：]\s*(.+)'
    for match in re.finditer(pattern, content):
        messages.append({
            "timestamp": match.group(1),
            "sender": match.group(2),
            "content": match.group(3)
        })
    
    return messages


def detect_patterns(messages: List[Dict], target_person: str = None) -> Dict:
    """检测有毒模式"""
    results = {
        "total_messages": len(messages),
        "patterns_found": defaultdict(list),
        "statistics": defaultdict(int),
        "timeline": [],
        "severity_score": 0
    }
    
    for msg in messages:
        content = msg.get("content", "")
        sender = msg.get("sender", "unknown")
        timestamp = msg.get("timestamp", "")
        
        # 如果指定了目标人物，只分析那个人的消息
        if target_person and sender != target_person:
            continue
        
        for pattern_type, pattern_info in TOXIC_PATTERNS.items():
            for pattern in pattern_info["patterns"]:
                if re.search(pattern, content, re.IGNORECASE):
                    results["patterns_found"][pattern_type].append({
                        "timestamp": timestamp,
                        "sender": sender,
                        "content": content,
                        "matched_pattern": pattern
                    })
                    results["statistics"][pattern_type] += 1
    
    # 计算严重程度分数 (0-100)
    total_detections = sum(results["statistics"].values())
    if total_detections > 0:
        # 根据检测到的模式类型和频率计算
        base_score = min(total_detections * 5, 50)
        type_diversity = len(results["patterns_found"]) * 10
        results["severity_score"] = min(base_score + type_diversity, 100)
    
    return results


def generate_report(results: Dict, output_file: str):
    """生成检测报告"""
    report = []
    report.append("=" * 60)
    report.append("🚩 有毒对话模式检测报告")
    report.append("=" * 60)
    report.append("")
    report.append(f"分析消息总数：{results['total_messages']}")
    report.append(f"检测到有毒模式：{sum(results['statistics'].values())} 次")
    report.append(f"严重程度评分：{results['severity_score']}/100")
    report.append("")
    
    # 严重程度评级
    if results['severity_score'] >= 80:
        rating = "🔴 高危 - 建议立即远离"
    elif results['severity_score'] >= 60:
        rating = "🟠 中高危 - 需要警惕"
    elif results['severity_score'] >= 40:
        rating = "🟡 中等 - 注意观察"
    elif results['severity_score'] >= 20:
        rating = "🟢 低 - 偶发情况"
    else:
        rating = "⚪ 极低 - 健康关系"
    
    report.append(f"评级：{rating}")
    report.append("")
    report.append("-" * 60)
    report.append("📊 模式统计")
    report.append("-" * 60)
    
    pattern_names = {
        "gaslighting": "煤气灯操纵",
        "blame_shifting": "甩锅",
        "emotional_manipulation": "情感操控",
        "silent_treatment": "冷暴力",
        "negging": "打压 (Negging)",
        "love_bombing": "爱意轰炸"
    }
    
    for pattern_type, count in sorted(results["statistics"].items(), key=lambda x: -x[1]):
        name = pattern_names.get(pattern_type, pattern_type)
        bar = "█" * min(count, 20)
        report.append(f"{name}: {count} {bar}")
    
    report.append("")
    report.append("-" * 60)
    report.append("📝 典型案例")
    report.append("-" * 60)
    
    for pattern_type, examples in results["patterns_found"].items():
        if examples:
            name = pattern_names.get(pattern_type, pattern_type)
            report.append(f"\n【{name}】")
            for ex in examples[:3]:  # 只显示前 3 个例子
                report.append(f"  > \"{ex['content']}\"")
    
    report.append("")
    report.append("=" * 60)
    report.append("💡 温馨提示：本检测仅供参考，不构成专业心理建议")
    report.append("如有需要，请寻求专业心理咨询师的帮助")
    report.append("=" * 60)
    
    report_text = "\n".join(report)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report_text)
    
    return report_text


def main():
    parser = argparse.ArgumentParser(description="有毒对话模式检测器")
    parser.add_argument("--input", required=True, help="聊天记录文件路径")
    parser.add_argument("--output", default="toxic_report.txt", help="报告输出路径")
    parser.add_argument("--target", help="目标分析对象（发送者名称）")
    parser.add_argument("--json", action="store_true", help="输出 JSON 格式报告")
    
    args = parser.parse_args()
    
    # 加载数据
    messages = load_chat_data(args.input)
    
    # 检测模式
    results = detect_patterns(messages, args.target)
    
    # 输出报告
    if args.json:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
    else:
        report = generate_report(results, args.output)
        print(report)


if __name__ == "__main__":
    main()
