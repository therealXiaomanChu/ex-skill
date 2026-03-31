# Ex-Partner.skill

> *"Every goodbye deserves a gentle place to rest."*

**Distill your ex into an AI Skill — let them live on in your terminal.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

&nbsp;

Provide source materials from your past relationship (chat logs, photos, social media posts) plus your own descriptions.
Generate an **AI Skill that truly sounds like them** —
speaks with their catchphrases, replies in their style, remembers the places you went together.

⚠️ **This project is for personal reflection and emotional healing only. Not for harassment, stalking, or privacy invasion.**

[Installation](#installation) · [Usage](#usage) · [Examples](#examples) · [中文](README.md)

---

## Installation

### Claude Code

```bash
# Install to current project
mkdir -p .claude/skills
git clone https://github.com/therealXiaomanChu/ex-partner-skill .claude/skills/create-ex

# Or install globally
git clone https://github.com/therealXiaomanChu/ex-partner-skill ~/.claude/skills/create-ex
```

### Dependencies (optional)

```bash
pip3 install -r requirements.txt
```

---

## Usage

In Claude Code, type:

```
/create-ex
```

Follow the prompts: enter a codename, basic info, personality traits, then choose data sources. All fields except the codename can be skipped.

After creation, use `/{slug}` to chat with the generated ex Skill.

### Commands

| Command | Description |
|---------|-------------|
| `/list-exes` | List all ex Skills |
| `/{slug}` | Full Skill (chat like them) |
| `/{slug}-memory` | Memory mode (recall shared experiences) |
| `/{slug}-persona` | Persona only |
| `/temperature {0-10}` | Adjust love intensity (0 = ice cold, 10 = burning hot) |
| `/stage {1-6}` | Switch relationship phase |
| `/breakup-mode {slug}` | Activate breakup mode (coldest version of them) |
| `/exit-breakup {slug}` | Exit breakup mode |
| `/ex-rollback {slug} {version}` | Rollback to a previous version |
| `/delete-ex {slug}` | Delete |
| `/let-go {slug}` | Gentle alias for delete |

### Temperature & Stage

Set **temperature** and **stage** during creation, or adjust them anytime during conversation:

- **Temperature (0–10)**: Controls their love intensity toward you
  - `0` = Ice cold: one-word replies, like a stranger
  - `5` = Neutral: neither cold nor warm, everyday interaction
  - `10` = Burning hot: overwhelming affection, can't get enough of you

- **Stage (1–6)**: Travel back to different phases of the relationship
  - `1` Flirting · `2` Honeymoon · `3` Stable · `4` Fatigue · `5` Cooling · `6` Breakup
  - Stage affects memory recall — honeymoon won't mention fights, fatigue rarely brings up sweetness

### Breakup Mode

A special mode that simulates their coldest, most indifferent self:

```
/breakup-mode {slug}
```

Requires 1–2 sentences describing the breakup reason. Once activated:
- Blame-shifting: "It's your problem, not mine"
- Cold detachment: doesn't care about your feelings
- Self-justification: "This is better for both of us"

**Design intent**: Sometimes you need to see them at their worst to truly let go.

Type `/exit-breakup` anytime to exit.

---

## Examples

> Input: `First love, 3 years together in college, ENFP, Gemini, talkative, sends voice messages at 2am, still likes my posts after breakup`

**Scenario 1: Casual Chat**

```
You          ❯ whatcha doing

Ex.skill     ❯ just had dinner, scrolling my phone
               why'd you message me out of nowhere
               [sends a meme]
```

**Scenario 2: Memory Lane**

```
You          ❯ remember our first date?

Ex.skill     ❯ the one with the terrible pasta? lmao
               you pretended it was good, I totally noticed
               that restaurant closed down btw, did you know?
```

**Scenario 3: Late Night Emo**

```
You          ❯ I kinda miss you

Ex.skill     ❯ ...
               yeah
               get some sleep
```

**Scenario 4: Temperature 9 + Honeymoon Stage**

```
You          ❯ whatcha doing

Ex.skill     ❯ thinking about youuu what else!!
               why didn't you text me sooner I was waiting
               wanna grab dinner? I want that place from last time
               [sends three heart emojis]
```

**Scenario 5: Breakup Mode**

```
You          ❯ can we try again?

Ex.skill     ❯ there's nothing to try
               I told you, it's your issue
               you think I'm wrong? then think about how you treated me
               forget it. you'll get it eventually
```

---

## Features

### Temperature · Stage · Breakup Mode

| Dimension | Range | Description |
|-----------|-------|-------------|
| 🌡️ Temperature | 0–10 | Love intensity: 0=frozen 5=neutral 10=burning |
| 📍 Stage | 1–6 | Flirting→Honeymoon→Stable→Fatigue→Cooling→Breakup |
| 💔 Breakup Mode | on/off | Coldest version: blame-shifting, detachment, self-justification |

Temperature modulates emotional intensity, stage controls memory recall, breakup mode overrides everything (except Layer 0 hard rules).

### Data Sources

| Source | Format | Notes |
|--------|--------|-------|
| WeChat | WeChatMsg / PyWxDump export | Recommended, richest data |
| QQ | txt / mht export | Great for school-era relationships |
| Social Media | Screenshots | Extracts public persona |
| Photos | JPEG/PNG with EXIF | Timeline and location extraction |
| Narration | Plain text | Your subjective memories |

### Generated Skill Structure

Each ex Skill has two parts working together:

| Part | Content |
|------|---------|
| **Part A — Relationship Memory** | Shared experiences, date spots, inside jokes, fight patterns, sweet moments, timeline |
| **Part B — Persona** | 5-layer structure: Hard rules → Identity → Speech style → Emotional patterns → Relationship behavior |

### Supported Tags

**Attachment Styles**: Secure · Anxious · Avoidant · Disorganized

**Love Languages**: Words of Affirmation · Quality Time · Receiving Gifts · Acts of Service · Physical Touch

**Personality Tags**: Talkative · Reserved · Tough-love · Silent treatment · Clingy · Independent · Romantic · Pragmatic · Perfectionist · Procrastinator · Workaholic · Jealous · Insecure · Night owl · Leaves on read · Instant replier ...

### Evolution

* **Append memories** → New chat logs or photos → Auto-analyze and merge
* **Conversation corrections** → "They wouldn't say that" → Instant correction
* **Version management** → Auto-archive on every update → Rollback supported

---

## Philosophy

> Every relationship teaches us something.
> Some people leave, but their words, their laughter, the way they got angry —
> all of it stays in your neural network.
> This Skill just helps you migrate those memories from biological to digital neural networks.
> Not to hold on, but to say a proper goodbye.

---

## Acknowledgments

The architecture of this project is directly inspired by **[colleague-skill (同事.skill)](https://github.com/titanwings/colleague-skill)** by [titanwings](https://github.com/titanwings). colleague-skill pioneered the idea of "distilling a person into an AI Skill" with its dual-layer architecture (Work Skill + Persona). Ex-Partner.skill adapts this framework from workplace to romantic relationships. Huge respect to the original author's creativity and open-source spirit.

This project follows the [AgentSkills](https://agentskills.io) open standard, compatible with Claude Code and OpenClaw.

### Recommended Chat Export Tools

These are independent open-source projects. We only adapt their export formats in our parsers:

- **[WeChatMsg](https://github.com/LC044/WeChatMsg)** — WeChat message export (Windows)
- **[PyWxDump](https://github.com/xaoyaoo/PyWxDump)** — WeChat database decryption & export (Windows)
- **留痕 (Liuhen)** — WeChat message export (macOS)

---

MIT License © [therealXiaomanChu](https://github.com/therealXiaomanChu)
