import re
from pathlib import Path


ROOT = Path(__file__).parents[1]
SKILL = ROOT / "SKILL.md"
COPILOT_ENTRYPOINT = ROOT / ".github" / "skills" / "create-ex" / "SKILL.md"


def test_skill_is_agent_skills_readable():
    content = SKILL.read_text(encoding="utf-8")
    assert content.startswith("---\n")
    assert re.search(r"(?m)^name:\s*create-ex\s*$", content)
    assert re.search(r"(?m)^description:\s*.+$", content)
    assert "${CLAUDE_SKILL_DIR}" not in content


def test_copilot_entrypoint_exists():
    content = COPILOT_ENTRYPOINT.read_text(encoding="utf-8")
    assert re.search(r"(?m)^name:\s*create-ex\s*$", content)
    assert "root" in content
    assert "`SKILL.md`" in content


def test_skill_does_not_require_claude_or_slash_commands():
    content = SKILL.read_text(encoding="utf-8").lower()
    assert "claude code" not in content
    assert "vendor-specific" in content
    assert "do not require a slash command" in content


def test_local_paths_and_privacy_contract_are_documented():
    content = SKILL.read_text(encoding="utf-8")
    assert "./exes/{slug}/" in content
    assert "Do not upload, publish, commit" in content
    assert "python3 tools/skill_writer.py" in content
