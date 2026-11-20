# ex.skill

> *"Every goodbye deserves a gentle place to rest."*

**Distill your ex into an AI Skill — let them live on in your terminal.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-Agent%20Skill-blueviolet)](https://github.com/features/copilot)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

&nbsp;

Provide source materials from your past relationship (chat logs, photos, social media posts) plus your own descriptions.
Generate an **AI Skill that truly sounds like them** —
speaks with their catchphrases, replies in their style, remembers the places you went together.

⚠️ **This project is for personal reflection and emotional healing only. Not for harassment, stalking, or privacy invasion.**

[Installation](#installation) · [Usage](#usage) · [Examples](#examples) · [中文](README.md)

---

## Installation

### GitHub Copilot / AgentSkills

```bash
# Clone into a workspace readable by Copilot
git clone https://github.com/therealXiaomanChu/ex-skill
cd ex-skill
```

### Dependencies (optional)

```bash
pip3 install -r requirements.txt
```

---

## Usage

In Copilot, use a natural-language request such as:

```
Help me create an ex skill
```

Follow the prompts: enter a codename, basic info, personality traits, then choose data sources. All fields except the codename can be skipped.

After creation, select the generated Skill using the Skill mechanism available in
your Copilot environment; slash commands are not required.

### Commands

| Command | Description |
|---------|-------------|
| `List all ex Skills` | List all ex Skills |
| `Talk to {slug}` | Full Skill |
| `Recall memories with {slug}` | Memory mode |
| `Analyze {slug}'s persona only` | Persona only |
| `Roll back {slug} to {version}` | Rollback |
| `Delete {slug}` | Delete after confirmation |

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

---

## Features

### Data Sources

| Source | Format | Notes |
|--------|--------|-------|
| WeChat | txt / html / json / csv exports | Recommended, richest data |
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

This project follows the [AgentSkills](https://agentskills.io) open standard and is
designed for GitHub Copilot's current workspace environment.

---

MIT License © [therealXiaomanChu](https://github.com/therealXiaomanChu)
