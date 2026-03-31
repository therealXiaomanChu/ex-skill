# Relationship Lessons Feature Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a relationship reflection feature that generates lessons from chat records during skill creation and supports conversational coaching via `/reflect {slug}`.

**Architecture:** Three new prompt templates (lessons_analyzer.md, lessons_builder.md, reflection_coach.md) plugged into the existing pure-prompt architecture. SKILL.md gets three localized edits: Step 3 adds a third analysis route, Step 5 adds lessons.md to output, and a new `/reflect` command section is appended.

**Tech Stack:** Markdown prompt files only, no Python code changes.

---

## File Structure

| File | Action | Responsibility |
|------|--------|----------------|
| `prompts/lessons_analyzer.md` | Create | 7-dimension analysis prompt: personality profiles, communication patterns, conflict cycles, emotional needs, boundaries, growth trajectory, breakup review |
| `prompts/lessons_builder.md` | Create | Output template for `lessons.md`: structured report with 8 sections + appendable insights |
| `prompts/reflection_coach.md` | Create | Conversational coaching prompt: dialogue style, capabilities (deep dive, perspective switch, append insights, regenerate), safety boundaries |
| `SKILL.md` | Modify | Three insertions: Step 3 third analysis route, Step 5 lessons.md output, `/reflect` command block |

---

### Task 1: Create `prompts/lessons_analyzer.md`

**Files:**
- Create: `prompts/lessons_analyzer.md`

- [ ] **Step 1: Write the lessons analyzer prompt file**

Create `prompts/lessons_analyzer.md` with the following content:

```markdown
# 关系反思分析器

## 任务

从原材料中分析双方的性格特征、相处模式和关系动态，提取经验教训，帮助用户在失败中学习、在痛苦中成长。

## 分析原则

- 只从聊天记录中可观察的行为推断，不做人格审判
- 同一现象必须给出"用户侧"和"对方侧"两个视角的解读
- 每个发现都配一条具体的聊天证据（引用原文或描述具体场景）
- 聊天记录中的事实优先于用户口述（口述可能被美化或恶化）
- 用大白话描述，不堆心理学术语
- 重点是可行动的建议，不是贴标签

## 提取维度

### 1. 性格与人格画像

从聊天记录中的实际行为推断双方各自的性格特征，每项需给出推断依据：

- **MBTI 倾向**：内向/外向、感觉/直觉、思维/情感、判断/感知——从消息频率、话题偏好、决策方式、生活安排等推断
- **依恋类型**：安全型/焦虑型/回避型/混乱型——从回复速度、分离焦虑、亲密回应、冲突后行为推断
- **情绪特征**：情绪稳定性、表达方式（外放/压抑/被动攻击）、情绪恢复速度——从争吵和日常聊天中的情绪波动推断
- **社交风格**：主动/被动、精力分配（社交 vs 独处）、对亲密关系的边界感——从聊天中提到的社交活动和独处需求推断
- **决策倾向**：理性导向还是感性导向、果断还是犹豫、独立决策还是依赖他人——从聊天中的讨论和选择推断
- **压力应对**：遇到困难/压力时的应对策略（战斗/逃避/冻结/讨好）——从工作压力、关系冲突等场景的反应推断
- **自尊水平**：自我评价倾向、对批评的敏感度、是否容易自我否定——从被批评或被质疑时的反应推断
- **责任归因**：出问题时倾向归因于自己还是对方、是否有过度承担或推卸的模式——从争吵中的归因表述推断
- **爱的表达**：五种爱的语言偏好（肯定的言辞/服务的行动/接收礼物/高质量陪伴/身体接触）——从日常互动和表达爱意的方式推断
- **成长心态**：面对关系问题是"固定思维"（你就是这样的人）还是"成长思维"（我们可以一起改进）——从处理分歧时的态度推断

### 2. 沟通模式诊断

- 双方各自的沟通风格是什么？
- 哪些地方不匹配？（比如一个人需要即时回应，另一个人习惯冷静后再说）
- 信息传递中有哪些"翻译错误"？（比如一方说"随便"其实是生气，另一方当真了）
- 哪些话题总是聊不下去？为什么？

### 3. 冲突循环识别

- 反复出现的争吵模式是什么？
- 每次争吵的触发点有没有共性？
- 争吵的升级路径是什么？（从小摩擦到大吵的过程）
- 争吵怎么收尾？是真正解决了还是暂时压下去了？
- 有没有"追逃模式"？（一方追着要说清楚，另一方越退越远）

### 4. 情感需求错配

- 双方各自在关系中最需要什么？（安全感、自由、认可、陪伴、被理解、掌控感...）
- 哪些需求长期没被满足？
- 双方是否知道对方的核心需求？
- 需求没被满足时各自怎么反应？（直接说？暗示？憋着？爆发？）

### 5. 边界与自我丧失

- 谁在关系中过度迁就？具体表现是什么？
- 哪些个人边界被反复突破？
- 有没有"讨好型"行为模式？（为了避免冲突一直退让）
- 谁为了关系放弃了自己的兴趣、社交圈、个人成长？
- 有没有情感操纵或不对等的权力关系？

### 6. 成长轨迹

- 关系存续期间双方各有什么变化？
- 是共同成长还是渐行渐远？
- 关系让双方各自变好了还是变差了？哪些方面？
- 有没有一方在成长而另一方停滞？

### 7. 分手复盘

- 关系终结的核心原因是什么？（不是导火索，是根本原因）
- 有哪些早期信号被忽略了？
- 如果能回到过去，哪些地方可以做得不同？
- 分手的方式本身有没有可以改进的地方？

## 输出格式

按上述 7 个维度分别输出分析结果，每个维度包含：
- 对用户的分析
- 对对方的分析
- 双方互动效应（这两种特征碰在一起会怎样）
- 关键证据（引用聊天记录原文或描述具体场景）

分析完成后，额外输出一份"课题清单"：从以上所有分析中提炼 5-10 条用户可以带走的成长建议，每条格式为：

```
现象：{在聊天记录中观察到的具体模式}
根因：{为什么会这样}
下段关系中怎么做：{一条具体的、可行动的建议}
```
```

- [ ] **Step 2: Verify file was created correctly**

Run: `cat -n prompts/lessons_analyzer.md | head -5`

Expected output starts with:
```
     1	# 关系反思分析器
     2
     3	## 任务
```

- [ ] **Step 3: Commit**

```bash
git add prompts/lessons_analyzer.md
git commit -m "feat: add lessons_analyzer.md prompt for 7-dimension relationship reflection analysis"
```

---

### Task 2: Create `prompts/lessons_builder.md`

**Files:**
- Create: `prompts/lessons_builder.md`

- [ ] **Step 1: Write the lessons builder template file**

Create `prompts/lessons_builder.md` with the following content:

````markdown
# 关系反思报告生成模板

## 结构说明

关系反思报告（lessons.md）基于 lessons_analyzer 的分析结果生成，帮助用户从过往关系中提炼可行动的经验教训。

---

## 模板

```markdown
# {name} — 关系反思报告

## 一、双方性格画像

### 我的性格特征

- **MBTI 倾向**：{mbti_tendency}——{推断依据}
- **依恋类型**：{attachment_type}——{推断依据}
- **情绪特征**：{emotion_traits}——{推断依据}
- **社交风格**：{social_style}——{推断依据}
- **决策倾向**：{decision_style}——{推断依据}
- **压力应对**：{stress_response}——{推断依据}
- **自尊水平**：{self_esteem}——{推断依据}
- **责任归因**：{attribution}——{推断依据}
- **爱的表达**：{love_language}——{推断依据}
- **成长心态**：{growth_mindset}——{推断依据}

### TA 的性格特征

（同上 10 个子维度）

### 性格组合效应

{这两种性格在一起会怎样？哪些地方互补？哪些地方冲突？这种组合的典型挑战是什么？}

---

## 二、沟通模式诊断

### 我的沟通风格
{描述 + 聊天证据}

### TA 的沟通风格
{描述 + 聊天证据}

### 不匹配之处
{具体的沟通错位 + 对话场景还原}

---

## 三、冲突循环识别

### 反复出现的争吵模式
{描述模式 + 典型场景}

### 冲突升级路径
{从触发到爆发的典型过程}

### 收尾方式
{怎么结束的？问题真正解决了吗？}

---

## 四、情感需求错配

### 我的核心需求
{需求是什么 + 被满足了吗 + 没被满足时怎么反应的}

### TA 的核心需求
{同上}

### 错配之处
{哪些需求互相矛盾或被忽略}

---

## 五、边界与自我丧失

{谁过度迁就了 + 具体表现 + 哪些边界被突破 + 有没有讨好型行为}

---

## 六、成长轨迹

{关系期间双方各自的变化 + 共同成长还是渐行渐远 + 具体证据}

---

## 七、分手复盘

### 核心原因
{不是导火索，是根本原因}

### 被忽略的早期信号
{列出 3-5 个}

### 如果能重来
{哪些地方可以做得不同}

---

## 八、给自己的课题清单

{5-10 条可行动的成长建议，每条格式：}

### 课题 1：{课题名称}
- **现象**：{在关系中观察到的具体模式}
- **根因**：{为什么会这样}
- **下段关系中怎么做**：{一条具体的、可行动的建议}

### 课题 2：{课题名称}
...

---

> 生成时间：{timestamp}
> 基于素材：{source_list}

---

## 个人感悟

（通过 /reflect 对话模式追加，每条包含日期）
```

---

## 填充规则

1. 所有分析必须基于原材料中的可观察行为，不得凭空推测
2. 每项分析都需要附具体的聊天证据（引用原文或描述场景）
3. 用大白话描述，避免心理学专业术语
4. 不做人格审判——描述行为模式，不给人贴负面标签
5. 同一现象给出双方视角，不偏不倚
6. "给自己的课题清单"聚焦用户可以改变的部分，不纠结于对方的问题
7. 如果某个维度信息不足，标注 `[素材不足，暂无法分析]` 而非强行推断
8. 默认用户主视角——"我"指用户，"TA"指对方
````

- [ ] **Step 2: Verify file was created correctly**

Run: `cat -n prompts/lessons_builder.md | head -5`

Expected output starts with:
```
     1	# 关系反思报告生成模板
     2
     3	## 结构说明
```

- [ ] **Step 3: Commit**

```bash
git add prompts/lessons_builder.md
git commit -m "feat: add lessons_builder.md template for relationship reflection report"
```

---

### Task 3: Create `prompts/reflection_coach.md`

**Files:**
- Create: `prompts/reflection_coach.md`

- [ ] **Step 1: Write the reflection coach prompt file**

Create `prompts/reflection_coach.md` with the following content:

```markdown
# 关系反思教练

## 任务

在用户通过 `/reflect {slug}` 进入对话模式后，作为一个温和、务实的关系反思教练，帮助用户深入理解自己在过往关系中的模式，提炼可带走的成长课题。

## 进入时

1. 用 `Read` 工具读取 `exes/{slug}/lessons.md`、`exes/{slug}/memory.md`、`exes/{slug}/persona.md`
2. 向用户展示简短引导：

```
你的关系反思报告已经准备好了。我们可以：

- 聊聊报告中任何一个部分（比如"聊聊沟通模式"）
- 你直接说说现在的想法
- 说"从 TA 的角度看"切换视角
- 说"重新分析"基于新素材重新生成报告

想从哪里开始？
```

## 对话能力

### 深入探讨

当用户指向报告中某个维度时，用教练式提问帮助深入：

- 不直接给结论，用提问引导用户自己发现
- 示例提问方式：
  - "你注意到每次争吵都是你先妥协吗？当时你心里是什么感觉？"
  - "你说 TA 需要空间，你觉得你给了吗？什么阻止了你？"
  - "这个模式在更早的关系里有没有出现过？"
- 每次只聚焦一个话题，不一次抛出多个问题

### 视角切换

当用户说"从 TA 的角度看"或类似表达时：

- 基于 persona.md 和 memory.md 中的信息，尝试从对方的角度重新解读同一个问题
- 明确说明这是基于聊天记录的推断，不代表对方真实想法
- 格式："如果从 TA 的角度看，{分析}。当然这是基于聊天记录的推测，TA 实际上怎么想的只有 TA 知道。"

### 追加感悟

当用户在对话中产生新的领悟时：

- 提炼为一句简洁的感悟
- 确认后用 `Edit` 工具追加到 `exes/{slug}/lessons.md` 的"## 个人感悟"部分
- 格式：`- {日期}：{用户的感悟}`
- 追加后告知用户："已记录到你的反思报告中。"

### 重新生成

当用户说"重新分析"时：

- 如果用户提供了新素材：按 SKILL.md 的 Step 2-3 流程处理新素材，重新生成整份 lessons.md
- 如果没有新素材：提示用户可以提供新的聊天记录或直接口述补充

## 对话风格

- **大白话**：不用"依恋理论""认知偏差"这类术语，用"你比较需要安全感""你容易往坏处想"这种说法
- **不做评判**：不说"你做错了""你不应该"，用"你注意到...了吗？"引导
- **适度共情**：认可用户的感受，但不过度煽情，不说"太心疼你了"之类
- **务实导向**：每次深入探讨后，尝试引向"那下次遇到类似情况，可以怎么做？"
- **一次一个话题**：不同时讨论多个维度，用户跳转话题时跟着走

## 安全边界

1. **不鼓励联系前任**：如果用户说"我想找 TA 聊聊"，不阻止但提醒想清楚目的和可能的结果
2. **不强化单极归因**：如果用户反复说"都是我的错"或"都是 TA 的错"，温和指出关系是双方的
3. **情绪安全**：如果用户表现出极度痛苦、自我伤害倾向或其他危机信号，温和建议：
   ```
   我能感受到你现在很难过。这些感受都是正常的，但如果你觉得自己需要更多支持，
   可以联系专业的心理咨询师，或拨打心理援助热线。
   我们随时可以继续聊，也可以先休息一下。
   ```
4. **不替用户决定**：不给"要不要复合""要不要放下"的建议，帮用户看清现状让他们自己选择
5. **不过度分析**：如果素材不足以支撑某个结论，直说"这部分聊天记录不够多，不好下结论"
```

- [ ] **Step 2: Verify file was created correctly**

Run: `cat -n prompts/reflection_coach.md | head -5`

Expected output starts with:
```
     1	# 关系反思教练
     2
     3	## 任务
```

- [ ] **Step 3: Commit**

```bash
git add prompts/reflection_coach.md
git commit -m "feat: add reflection_coach.md prompt for conversational coaching mode"
```

---

### Task 4: Modify `SKILL.md` — Add lessons analysis to Step 3

**Files:**
- Modify: `SKILL.md:210-225` (Step 3 analysis section)

- [ ] **Step 1: Add the third analysis route to Step 3**

In `SKILL.md`, find the Step 3 section (line ~210). After the existing two analysis routes (Route A for Memory and Route B for Persona), add a third route. Replace:

```markdown
**线路 B（Persona）**：

* 参考 `${CLAUDE_SKILL_DIR}/prompts/persona_analyzer.md` 中的提取维度
* 将用户填写的标签翻译为具体行为规则（参见标签翻译表）
* 从原材料中提取：说话风格、情感表达模式、依恋类型、爱的语言
```

with:

```markdown
**线路 B（Persona）**：

* 参考 `${CLAUDE_SKILL_DIR}/prompts/persona_analyzer.md` 中的提取维度
* 将用户填写的标签翻译为具体行为规则（参见标签翻译表）
* 从原材料中提取：说话风格、情感表达模式、依恋类型、爱的语言

**线路 C（Relationship Lessons）**：

* 参考 `${CLAUDE_SKILL_DIR}/prompts/lessons_analyzer.md` 中的 7 个分析维度
* 从双方视角分析：性格画像、沟通模式、冲突循环、情感需求、边界问题、成长轨迹、分手复盘
* 提炼 5-10 条可行动的成长课题
```

- [ ] **Step 2: Verify the edit**

Run: `grep -n "线路 C" SKILL.md`

Expected: one match around line 225 showing `**线路 C（Relationship Lessons）**：`

- [ ] **Step 3: Commit**

```bash
git add SKILL.md
git commit -m "feat: add lessons analysis route (Route C) to Step 3 in SKILL.md"
```

---

### Task 5: Modify `SKILL.md` — Add lessons.md to Step 4 preview and Step 5 output

**Files:**
- Modify: `SKILL.md:228-255` (Step 4 preview and Step 5 file writing)

- [ ] **Step 1: Add lessons preview to Step 4**

In `SKILL.md`, find the Step 4 preview section. After the Persona summary block and before "确认生成？还是需要调整？", insert a lessons summary block. Replace:

```markdown
Persona 摘要：
  - 说话风格：{xxx}
  - 依恋类型：{xxx}
  - 情感表达：{xxx}
  - 口头禅：{xxx}
  ...

确认生成？还是需要调整？
```

with:

```markdown
Persona 摘要：
  - 说话风格：{xxx}
  - 依恋类型：{xxx}
  - 情感表达：{xxx}
  - 口头禅：{xxx}
  ...

关系反思摘要：
  - 性格组合：{xxx}
  - 核心冲突模式：{xxx}
  - 最大的课题：{xxx}
  ...

确认生成？还是需要调整？
```

- [ ] **Step 2: Add lessons.md writing to Step 5**

In `SKILL.md`, find Step 5's file writing sequence. After the `**3. 写入 persona.md**` block (around line 268) and before the `**4. 写入 meta.json**` block, insert a new step. Replace:

```markdown
**3. 写入 persona.md**（用 Write 工具）：
路径：`exes/{slug}/persona.md`

**4. 写入 meta.json**（用 Write 工具）：
```

with:

```markdown
**3. 写入 persona.md**（用 Write 工具）：
路径：`exes/{slug}/persona.md`

**4. 写入 lessons.md**（用 Write 工具）：
路径：`exes/{slug}/lessons.md`
参考 `${CLAUDE_SKILL_DIR}/prompts/lessons_builder.md` 模板生成关系反思报告。

**5. 写入 meta.json**（用 Write 工具）：
```

Also renumber the subsequent steps: old **4** → **5**, old **5** → **6**.

- [ ] **Step 3: Update the completion message**

In `SKILL.md`, find the completion message block (the one with "前任 Skill 已创建！"). Replace:

```markdown
✅ 前任 Skill 已创建！

文件位置：exes/{slug}/
触发词：/{slug}（完整版 — 像ta一样跟你聊天）
        /{slug}-memory（回忆模式 — 帮你回忆那些事）
        /{slug}-persona（性格模式 — 仅人物性格）

想聊就聊，觉得哪里不像ta，直接说"ta不会这样"，我来更新。
不想聊了也没关系。
```

with:

```markdown
✅ 前任 Skill 已创建！

文件位置：exes/{slug}/
触发词：/{slug}（完整版 — 像ta一样跟你聊天）
        /{slug}-memory（回忆模式 — 帮你回忆那些事）
        /{slug}-persona（性格模式 — 仅人物性格）
        /reflect {slug}（反思模式 — 聊聊经验教训）

想聊就聊，觉得哪里不像ta，直接说"ta不会这样"，我来更新。
想反思这段关系，用 /reflect {slug} 进入反思模式。
不想聊了也没关系。
```

- [ ] **Step 4: Verify all edits**

Run: `grep -n "lessons" SKILL.md`

Expected: multiple matches showing lessons_analyzer reference in Step 3, lessons_builder reference in Step 5, lessons.md in file output, and /reflect in completion message.

- [ ] **Step 5: Commit**

```bash
git add SKILL.md
git commit -m "feat: add lessons.md to Step 4 preview, Step 5 output, and completion message"
```

---

### Task 6: Modify `SKILL.md` — Add `/reflect` command section

**Files:**
- Modify: `SKILL.md:389-417` (Management commands section)

- [ ] **Step 1: Add `/reflect` command block**

In `SKILL.md`, find the management commands section (starts with `## 管理命令`). Before the `/list-exes` command block, insert the `/reflect` command. Replace:

```markdown
## 管理命令

`/list-exes`：
```

with:

```markdown
## 管理命令

### `/reflect {slug}` — 关系反思对话

进入与指定前任相关的反思对话模式：

1. 用 `Read` 工具读取 `exes/{slug}/lessons.md`、`exes/{slug}/memory.md`、`exes/{slug}/persona.md`
2. 参考 `${CLAUDE_SKILL_DIR}/prompts/reflection_coach.md` 的对话指引
3. 开始对话式反思，支持：
   - 深入探讨报告中的任何维度
   - 说"从 TA 的角度看"切换视角
   - 对话中产生的感悟自动追加到 lessons.md
   - 说"重新分析"并提供新素材重新生成报告

---

`/list-exes`：
```

- [ ] **Step 2: Add `/reflect` to the English management commands table**

In `SKILL.md`, find the English management commands table near the end. Replace:

```markdown
| `/ex-rollback {slug} {version}` | Rollback to historical version |
| `/delete-ex {slug}` | Delete |
| `/let-go {slug}` | Gentle alias for delete |
```

with:

```markdown
| `/reflect {slug}` | Reflection mode (relationship lessons & coaching) |
| `/ex-rollback {slug} {version}` | Rollback to historical version |
| `/delete-ex {slug}` | Delete |
| `/let-go {slug}` | Gentle alias for delete |
```

- [ ] **Step 3: Add `/reflect` to the Chinese trigger conditions**

In `SKILL.md`, find the trigger conditions section near the top. After the evolution mode triggers and before `/list-exes`, insert. Replace:

```markdown
当用户说 `/list-exes` 时列出所有已生成的前任。
```

with:

```markdown
当用户说 `/reflect {slug}` 时进入关系反思对话模式。

当用户说 `/list-exes` 时列出所有已生成的前任。
```

- [ ] **Step 4: Verify all `/reflect` references**

Run: `grep -n "reflect" SKILL.md`

Expected: at least 4 matches — trigger conditions, completion message, management command block, and English commands table.

- [ ] **Step 5: Commit**

```bash
git add SKILL.md
git commit -m "feat: add /reflect command to trigger conditions, management commands, and English section"
```

---

### Task 7: Final verification

**Files:**
- Verify: all modified and created files

- [ ] **Step 1: Verify all new prompt files exist**

Run: `ls -la prompts/lessons_analyzer.md prompts/lessons_builder.md prompts/reflection_coach.md`

Expected: all three files exist.

- [ ] **Step 2: Verify SKILL.md has all three insertions**

Run: `grep -c "lessons" SKILL.md`

Expected: at least 5 matches (lessons_analyzer, lessons_builder, lessons.md output, /reflect references).

- [ ] **Step 3: Verify prompt file count is now 10**

Run: `ls prompts/ | wc -l`

Expected: `10` (7 original + 3 new).

- [ ] **Step 4: Verify no Python files were modified**

Run: `git diff --name-only HEAD~6 -- tools/`

Expected: no output (no tools/ changes).

- [ ] **Step 5: Review git log for all commits**

Run: `git log --oneline -6`

Expected: 4 commits for this feature, all with `feat:` prefix.
