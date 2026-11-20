---
name: create-ex
description: Create a private, local AI Skill from relationship memories, chat exports, photos, and social posts. Produces relationship memory, persona, and a runnable generated Skill.
argument-hint: [ex-name-or-slug]
user-invocable: true
---

# Ex Skill Creator

This is an Agent Skill for GitHub Copilot and other AgentSkills-compatible hosts.
It supports Chinese and English: detect the user's language from the first message
and keep the same language throughout.

The skill may be invoked by a natural-language request such as “create an ex
skill”, “distill an ex”, or “make a skill for …”. Do not require a slash command.
If the host supports slash invocation, `/create-ex` is optional convenience syntax,
not a requirement. Likewise, generated skills are selected by their name or by
natural language; do not depend on `/{slug}` commands.

## Host and file handling

- Use the host's available workspace file-reading and file-writing tools. Do not
  assume vendor-specific tool names such as `Read`, `Write`, or `Edit`.
- Use the host's terminal tool for the Python helpers in `tools/`. Run commands
  from this repository's root, or replace `tools/...` with the absolute path to
  this checked-out skill repository. Never use a host-specific skill-directory
  variable.
- Generated data belongs under `./exes/{slug}/`. Keep source files where the user
  placed them unless a copy is explicitly needed for analysis. Use a temporary
  directory for intermediate parser output and delete it when finished.
- Treat user-provided files as private. Do not upload, publish, commit, or send
  them to any external service. Do not inspect unrelated files.
- Never put real names, chat logs, photos, or other private source material in
  tests, examples, documentation, or tool output.

## Safety boundaries

1. Personal reflection and emotional healing only; never harassment, stalking, or
   privacy invasion.
2. The generated Skill simulates a conversation and must not contact or impersonate
   a real person.
3. If the user shows unhealthy fixation or intent to contact someone, respond
   gently and suggest distance or professional support.
4. Preserve uncertainty. Do not invent memories, motives, diagnoses, or events.
5. Layer 0 is highest priority: do not make the simulated person say things they
   would not plausibly say unless source evidence supports it.

## Creation flow

### 1. Collect the minimum profile

Ask, one at a time:

1. A codename or alias (required; a real name is unnecessary).
2. Basic context: relationship duration, time since separation, occupation or
   other useful context.
3. A personality impression: traits, MBTI/zodiac if the user wants, speech habits,
   and emotional style.

Only the codename is required. Summarize the answers and ask for confirmation
before processing source material.

### 2. Import optional source material

Offer these choices, which can be mixed or skipped:

- WeChat exports (`txt`, `csv`, `html`, `json`)
- QQ exports (`txt`, `mht`)
- Social posts or screenshots
- Photos, PDFs, or text files
- Pasted or narrated memories

When a user provides a path, validate that it exists and is in scope before
reading it. For image/PDF inputs, use the host's file or image-reading capability
when available. For text exports, use the local helpers:

```bash
python3 tools/wechat_parser.py --file "<path>" --target "<name>" \
  --output "<temporary-output>" --format auto
python3 tools/qq_parser.py --file "<path>" --target "<name>" \
  --output "<temporary-output>"
python3 tools/social_parser.py --dir "<directory>" \
  --output "<temporary-output>"
python3 tools/photo_analyzer.py --dir "<directory>" \
  --output "<temporary-output>"
```

The helpers only process local paths. Do not treat their output as verified fact:
separate direct evidence from the user's interpretation and mark uncertainty.

### 3. Analyze into two independent parts

Use the templates in `prompts/memory_analyzer.md` and
`prompts/persona_analyzer.md`.

- **Relationship Memory:** timeline, shared experiences, routines, preferences,
  places, conflict patterns, affectionate moments, and inside jokes.
- **Persona:** speech style, catchphrases, punctuation, emotional expression,
  attachment patterns, values, boundaries, and likely responses.

Do not infer sensitive traits or private facts that are not needed for the user's
request. Ask for clarification when evidence conflicts.

### 4. Preview before writing

Use `prompts/memory_builder.md` and `prompts/persona_builder.md` to produce
drafts. Show a short summary of each part and ask the user to confirm or correct
it. Do not write generated files before confirmation.

### 5. Write the generated Skill

After confirmation, initialize the local directory:

```bash
python3 tools/skill_writer.py --action init --slug "<slug>" --base-dir ./exes
```

Write these files under `exes/{slug}/`:

- `memory.md`: relationship memory
- `persona.md`: persona and response rules
- `meta.json`: alias, timestamps, profile, source categories, and version
- `SKILL.md`: combined runnable Skill
- `memories/chats`, `memories/photos`, and `memories/social`: optional local
  source artifacts or derived notes, only when the user explicitly wants them

The generated `SKILL.md` must:

1. Follow the same language and persona rules as the source material.
2. Treat the persona as a simulation, not the real person or an assistant with
   authority over the user's life.
3. Use persona first for tone and likely attitude, then memory for context.
4. Preserve uncertainty and never fabricate a memory.
5. Keep Layer 0 boundaries: no implausible confession, apology, reconciliation,
   or unconditional acceptance without evidence.

Combine the two parts with the local helper:

```bash
python3 tools/skill_writer.py --action combine --slug "<slug>" --base-dir ./exes
```

Tell the user where the files were written and how to select the generated Skill
in their Copilot workspace. Do not promise a slash command unless the host
explicitly supports it.

## Evolution flow

When the user supplies additional memories or files:

1. Read only the new material and the relevant existing `memory.md`/`persona.md`.
2. Use `prompts/merger.md` to classify additions and resolve conflicts.
3. Back up the current version:

   ```bash
   python3 tools/version_manager.py --action backup --slug "<slug>" --base-dir ./exes
   ```
4. Update the smallest relevant file, update `meta.json`, and recombine `SKILL.md`.
5. Show the user a concise change summary and preserve uncertainty.

When the user says the simulation is wrong, use
`prompts/correction_handler.md`, classify the correction as Memory or Persona,
append a dated correction record, and recombine the Skill. Never silently replace
source-backed facts.

## Local management

To list generated Skills:

```bash
python3 tools/skill_writer.py --action list --base-dir ./exes
```

To list or roll back versions:

```bash
python3 tools/version_manager.py --action list --slug "<slug>" --base-dir ./exes
python3 tools/version_manager.py --action rollback --slug "<slug>" \
  --version "<version>" --base-dir ./exes
```

For deletion, confirm the exact slug and then delete only that
`exes/{slug}/` directory with the host's file operation. Never use a broad
recursive deletion and never delete source files outside that directory.

## Reference files

The following files are local implementation references, not host-specific
commands:

- `prompts/intake.md`
- `prompts/memory_analyzer.md`
- `prompts/persona_analyzer.md`
- `prompts/memory_builder.md`
- `prompts/persona_builder.md`
- `prompts/merger.md`
- `prompts/correction_handler.md`
