# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

ex-skill（原名 ex-partner-skill）是一个 Claude Code 元技能（meta-skill），用于将过往恋爱关系的原始素材（微信/QQ 聊天记录、照片、社交媒体帖子、个人叙述）转化为可独立运行的 AI Skill，模拟前任的说话风格、情感模式和共同记忆。用于个人情感反思与疗愈，内置安全边界。

## 项目上下文

本项目使用 Kontext 生成了结构化上下文，存放在 `.kontext/` 目录中。开始任务前请先阅读以下制品：

- `.kontext/PROJECT_MANIFEST.json` — 项目清单（定位、技术栈、核心流程）
- `.kontext/ARCHITECTURE_MAP.json` — 架构分层与模块归属
- `.kontext/CONVENTIONS.json` — 编码规范与约束
- `.kontext/module_contracts/` — 各模块的职责边界与接口契约

请基于这些上下文理解项目结构后再进行开发。

## 运行方式

这不是传统应用程序，没有构建步骤。项目作为 Claude Code Skill 运行，入口文件是 `SKILL.md`。

**安装到项目：**
```bash
mkdir -p .claude/skills
git clone <repo> .claude/skills/create-ex
pip3 install -r requirements.txt  # 可选，仅 Pillow 用于照片 EXIF 读取
```

**触发命令：**
- `/create-ex` — 创建新的前任技能（5 步流程）
- `/list-exes` — 列出所有已生成的前任技能
- `/{slug}` — 与生成的前任技能对话（完整模式）
- `/update-ex {slug}` — 进入演化模式（追加素材）
- `/ex-rollback {slug} {version}` — 回滚到历史版本
- `/delete-ex {slug}` — 删除已生成的技能

**单独运行 Python 工具：**
```bash
python3 tools/wechat_parser.py --file <path> --target <name> --output <output_path>
python3 tools/qq_parser.py --file <path> --target <name> --output <output_path>
python3 tools/social_parser.py --dir <dir> --output <output_path>
python3 tools/photo_analyzer.py --dir <dir> --output <output_path>
python3 tools/skill_writer.py --action list --base-dir ./exes
python3 tools/version_manager.py --action backup --slug <slug> --base-dir ./exes
```

## 架构

项目采用 6 层架构，层间单向依赖：

1. **入口编排层**（`SKILL.md`）— 主控制器，定义触发条件、5 步创建流程、演化模式、管理命令和安全边界。Claude Code 直接解释执行此文件。
2. **提示词模板层**（`prompts/`）— 7 个无状态 Markdown 文件，定义各阶段的 LLM 提示词模板，通过 `${CLAUDE_SKILL_DIR}/prompts/xxx.md` 引用。
3. **数据解析工具层**（`tools/wechat_parser.py`、`qq_parser.py`、`social_parser.py`、`photo_analyzer.py`）— 独立 Python CLI 工具，将原始素材解析为结构化数据，输出到 `/tmp/`。
4. **文件管理工具层**（`tools/skill_writer.py`、`version_manager.py`）— 管理 `exes/{slug}/` 下的生成文件，包括目录初始化、文件合并、版本备份和回滚。
5. **生成产物层**（`exes/{slug}/`）— 运行时输出：`SKILL.md`、`memory.md`、`persona.md`、`meta.json`、`versions/`、`memories/`。
6. **文档层**（`docs/`、`README.md`）— 产品规格和文档，无运行时作用。

## 核心设计模式

- **双部件架构**：每个生成的技能包含 Part A（关系记忆，事实性）和 Part B（人设，行为性），可独立或组合使用。
- **5 层人设优先级**：Layer 0（硬规则）> Layer 1（身份）> Layer 2（说话方式）> Layer 3（情感模式）> Layer 4（关系行为）。高层不可被低层覆盖。
- **演化机制**：记忆追加（不覆盖）、对话修正（Correction 记录跟踪）、自动版本归档与回滚。
- **标签翻译模式**：`persona_analyzer.md` 中将抽象人格标签（如"话痨"、"冷暴力"）翻译为具体行为规则。
- **优雅降级**：可选依赖 Pillow 使用 try/except 导入，格式自动检测失败时回退到纯文本。

## 依赖说明

- Python 3.9+，核心功能仅使用标准库（`argparse`、`json`、`re`、`os`、`pathlib`、`datetime`、`shutil`）
- `Pillow>=9.0.0` — 唯一外部依赖，可选，用于照片 EXIF 读取
- 所有 Python 工具为独立 CLI，模块间零耦合

## 未完成功能

- 微信 HTML/CSV 格式解析（格式检测已实现，解析函数未实现）
- PyWxDump SQLite 格式解析（格式检测已实现，解析函数缺失）
- 示例技能 `exes/example_xiaoming/` 尚未创建
- 无测试套件、无 CI/CD 管线
