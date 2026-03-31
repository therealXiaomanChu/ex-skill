# 前任.skill

> *"你们搞大模型的简直是码神，你们解放了前端兄弟，还要解放后端兄弟，测试兄弟，运维兄弟，解放网安兄弟，解放ic兄弟，最后解放自己解放全人类"*

**我会为了你一万次回到那个夏天。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

&nbsp;

提供前任的原材料（微信聊天记录、QQ消息、朋友圈截图、照片）加上你的主观描述  
生成一个**真正像ta的 AI Skill**  
用ta的口头禅说话，用ta的方式回复你，记得你们一起去过的地方

⚠️ **本项目仅用于个人回忆与情感疗愈，不用于骚扰、跟踪或侵犯他人隐私。**

[安装](#安装) · [使用](#使用) · [效果示例](#效果示例) · [English](README_EN.md)

---

## 安装

### Claude Code

> **重要**：Claude Code 从 **git 仓库根目录** 的 `.claude/skills/` 查找 skill。请在正确的位置执行。

```bash
# 安装到当前项目（在 git 仓库根目录执行）
mkdir -p .claude/skills
git clone https://github.com/therealXiaomanChu/ex-partner-skill .claude/skills/create-ex

# 或安装到全局（所有项目都能用）
git clone https://github.com/therealXiaomanChu/ex-partner-skill ~/.claude/skills/create-ex
```

### 依赖（可选）

```bash
pip3 install -r requirements.txt
```

---

## 使用

在 Claude Code 中输入：

```
/create-ex
```

按提示输入前任的代号、基本信息、性格画像，然后选择数据来源。所有字段均可跳过，仅凭描述也能生成。

完成后用 `/{slug}` 调用该前任 Skill，开始对话。

### 管理命令

| 命令 | 说明 |
|------|------|
| `/list-exes` | 列出所有前任 Skill |
| `/{slug}` | 调用完整 Skill（像ta一样跟你聊天） |
| `/{slug}-memory` | 回忆模式（帮你回忆那些事） |
| `/{slug}-persona` | 仅人物性格 |
| `/temperature {0-10}` | 调整爱意浓度（0=冰点，10=沸腾） |
| `/stage {1-6}` | 切换关系阶段 |
| `/breakup-mode {slug}` | 开启分手模式（最冷漠的ta） |
| `/exit-breakup {slug}` | 退出分手模式 |
| `/ex-rollback {slug} {version}` | 回滚到历史版本 |
| `/delete-ex {slug}` | 删除 |
| `/let-go {slug}` | 放下（delete 的温柔别名） |

### 温度与阶段

创建 Skill 时可以设定**温度**和**阶段**，运行中也可以随时调节：

- **温度（0–10）**：控制ta对你的爱意浓度
  - `0` = 冰点：一个字回复，像陌生人
  - `5` = 日常：不冷不热，正常互动
  - `10` = 沸腾：爱到发烫，恨不得每秒在一起

- **阶段（1–6）**：回到关系的不同时期
  - `1` 暧昧期 · `2` 热恋期 · `3` 稳定期 · `4` 倦怠期 · `5` 冷淡期 · `6` 分手期
  - 阶段影响记忆调用——热恋期不会提争吵，倦怠期不怎么提甜蜜

### 分手模式

一个特殊模式，模拟ta在分手时最冷漠的样子：

```
/breakup-mode {slug}
```

开启前需要提供 1–2 句分手原因。开启后ta会：
- 推卸责任，把问题归到你身上
- 冷漠疏离，不再在意你的感受
- 自我合理化，"这样对我们都好"

**设计初衷**：有时候你需要看到ta最差的样子，才能真正说服自己放下。

⚠️ 如果你感到不适，随时输入 `/exit-breakup` 退出。

---

## 效果示例

> 输入：`初恋，在一起三年，大学时期，ENFP，双子座，话痨，半夜给我发语音，分手后还给我点赞`

**场景一：日常聊天**

```
用户      ❯ 在干嘛

前任.skill ❯ 刚吃完饭 在刷手机
             你呢 怎么突然找我
             [发送了一个表情包]
```

**场景二：回忆杀**

```
用户      ❯ 还记得我们第一次约会吗

前任.skill ❯ 就那个超难吃的意面吗哈哈哈哈
             你还假装很好吃 我都看出来了
             那家店后来倒闭了你知道吗
```

**场景三：深夜emo**

```
用户      ❯ 我有点想你

前任.skill ❯ ...
             嗯
             早点睡吧
```

**场景四：吵架模式**

```
用户      ❯ 你当时为什么不回我消息

前任.skill ❯ 又来了
             我说了我在忙 你非要这样
             算了不想吵
```

**场景五：温度 9 + 热恋期**

```
用户      ❯ 在干嘛

前任.skill ❯ 在想你啊还能干嘛！！
             你今天怎么才找我 我等了好久
             晚上出来吃饭吗 我想吃上次那家
             [发送了三个爱心表情]
```

**场景六：分手模式**

```
用户      ❯ 我们能不能再试试

前任.skill ❯ 没什么好试的
             我说过了 是你自己的问题
             你觉得我说得不对？那你想想你之前怎么对我的
             算了 不想说了 你以后会懂的
```

---

## 功能特性

### 数据源

| 来源 | 格式 | 备注 |
|------|------|------|
| 微信聊天记录 | WeChatMsg / 留痕 / PyWxDump 导出 | 推荐，信息最丰富 |
| QQ 聊天记录 | txt / mht 导出 | 适合学生时代的恋情 |
| 朋友圈/微博 | 截图 | 提取公开人设 |
| 照片 | JPEG/PNG（含 EXIF） | 提取时间线和地点 |
| 口述/粘贴 | 纯文本 | 你的主观记忆 |

### 生成的 Skill 结构

每个前任 Skill 由两部分组成，共同驱动输出：

| 部分 | 内容 |
|------|------|
| **Part A — Relationship Memory** | 共同经历、约会地点、inside jokes、争吵模式、甜蜜瞬间、关系时间线 |
| **Part B — Persona** | 5 层性格结构：硬规则 → 身份 → 说话风格 → 情感模式 → 关系行为 |

运行逻辑：`收到消息 → Persona 判断ta会怎么回 → Memory 补充共同记忆 → 用ta的方式输出`

### 温度 · 阶段 · 分手模式

| 维度 | 范围 | 说明 |
|------|------|------|
| 🌡️ 温度 | 0–10 | 爱意浓度：0=冰点 5=日常 10=沸腾 |
| 📍 阶段 | 1–6 | 暧昧→热恋→稳定→倦怠→冷淡→分手 |
| 💔 分手模式 | 开/关 | 最冷漠的ta：推责、冷漠、自我合理化 |

温度影响情感浓度，阶段影响记忆调用，分手模式覆盖一切（除 Layer 0 硬规则）。

### 支持的标签

**依恋类型**：安全型 · 焦虑型 · 回避型 · 混乱型

**爱的语言**：肯定的言辞 · 精心的时刻 · 接受礼物 · 服务的行动 · 身体的接触

**性格标签**：话痨 · 闷骚 · 嘴硬心软 · 冷暴力 · 粘人 · 独立 · 大男/女子主义 · 浪漫主义 · 实用主义 · 完美主义 · 拖延症 · 工作狂 · 控制欲 · 没有安全感 · 报复性熬夜 · 已读不回 · 秒回选手 · 朋友圈三天可见 · 半夜发语音 …

**星座**：十二星座全支持，影响性格标签的翻译规则

**MBTI**：16 型全支持，影响沟通风格和决策模式

### 进化机制

* **追加记忆** → 找到更多聊天记录/照片 → 自动分析增量 → merge 进对应部分
* **对话纠正** → 说「ta不会这样说」→ 写入 Correction 层，立即生效
* **版本管理** → 每次更新自动存档，支持回滚

---

## 项目结构

本项目遵循 [AgentSkills](https://agentskills.io) 开放标准：

```
create-ex/
├── SKILL.md                # skill 入口（官方 frontmatter）
├── prompts/                # Prompt 模板
│   ├── intake.md           #   对话式信息录入
│   ├── memory_analyzer.md  #   关系记忆提取
│   ├── persona_analyzer.md #   性格行为提取（含标签翻译表）
│   ├── memory_builder.md   #   memory.md 生成模板
│   ├── persona_builder.md  #   persona.md 五层结构模板
│   ├── merger.md           #   增量 merge 逻辑
│   ├── correction_handler.md # 对话纠正处理
│   ├── temperature_stages.md # 温度与阶段系统
│   └── breakup_mode.md     #   分手模式
├── tools/                  # Python 工具
│   ├── wechat_parser.py    # 微信聊天记录解析
│   ├── qq_parser.py        # QQ 聊天记录解析
│   ├── social_parser.py    # 社交媒体内容解析
│   ├── photo_analyzer.py   # 照片元信息分析
│   ├── skill_writer.py     # Skill 文件管理
│   └── version_manager.py  # 版本存档与回滚
├── exes/                   # 生成的前任 Skill（gitignored）
├── docs/PRD.md
├── requirements.txt
└── LICENSE
```

---

## 注意事项

* **聊天记录质量决定还原度**：微信导出 + 口述 > 仅口述
* 建议优先提供：**深夜对话** > **争吵记录** > **日常消息**（最能体现真实性格）
* 本项目不鼓励对前任的不健康执念，如果你发现自己过于沉浸，请寻求专业帮助
* 你的前任是一个真实的人，ta有自己的人生。这个 Skill 只是你记忆中的ta


---

### 推荐的聊天记录导出工具

以下工具为独立的开源项目，本项目不包含它们的代码，仅在解析器中适配了它们的导出格式：

- **[WeChatMsg](https://github.com/LC044/WeChatMsg)** — 微信聊天记录导出（Windows）
- **[PyWxDump](https://github.com/xaoyaoo/PyWxDump)** — 微信数据库解密导出（Windows）
- **留痕** — 微信聊天记录导出（macOS）
## 致敬 & 引用

本项目的架构灵感直接来源于 **[同事.skill](https://github.com/titanwings/colleague-skill)**（by [titanwings](https://github.com/titanwings)）。同事.skill 首创了"把人蒸馏成 AI Skill"的双层架构（Work Skill + Persona），前任.skill 在此基础上将场景从职场迁移到了恋爱关系。致敬原作者的创意和开源精神。

本项目遵循 [AgentSkills](https://agentskills.io) 开放标准，兼容 Claude Code 和 OpenClaw。

---

### 推荐的聊天记录导出工具

以下工具为独立的开源项目，本项目不包含它们的代码，仅在解析器中适配了它们的导出格式：

- **[WeChatMsg](https://github.com/LC044/WeChatMsg)** — 微信聊天记录导出（Windows）
- **[PyWxDump](https://github.com/xaoyaoo/PyWxDump)** — 微信数据库解密导出（Windows）
- **留痕** — 微信聊天记录导出（macOS）

---

### 写在最后
人的记忆是一种不讲道理的存储介质。
你记不住高数公式，记不住车牌号，记不住今天是几号，但你清楚记得四年前的一个下午ta穿了一件白T恤站在便利店门口等你，手里拿着两根冰棍，一根给你，一根ta自己。
这不公平。
这个 Skill 就是把这些不公平的记忆导出来，从生物硬盘到数字硬盘完成格式转换。
导完以后你或许会发现，ta也没那么好。ta也没那么差。ta就是那样一个人。会在吵完架两小时后问你吃了吗。会在纪念日那天忘了发消息然后第二天假装什么都没发生。
是的，
此刻，阳光在江面碎成一万个夏天，闪烁，又汇聚成一个冬天。这一切在你午睡时发生，你从未察觉。

MIT License © [therealXiaomanChu](https://github.com/therealXiaomanChu)
