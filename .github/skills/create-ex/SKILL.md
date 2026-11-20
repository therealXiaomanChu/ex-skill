---
name: create-ex
description: Create a private, local AI Skill from relationship memories, chat exports, photos, and social posts.
user-invocable: true
---

# Copilot entrypoint

This repository's complete, provider-neutral skill definition is the root
`SKILL.md`. Read that file and follow it as the source of truth. It defines the
creation, import, memory, persona, evolution, local-file, and privacy workflow.

Do not assume vendor-specific tool names, host-specific path variables, or slash
commands. All generated user data must remain under `./exes/{slug}/` and must not
be uploaded, published, committed, or included in tests and documentation.
