"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
Deterministic, no network, stdlib only.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The fortune: an agent's context window remembers the whole conversation
# except the one fact it actually needs — the classic retrieval failure,
# served as a cookie.
ENTRY = "Your context window will hold everything except the one detail that matters."


def validate_entry(text: str) -> str:
    """One-line fortune: non-empty, single line, no stray whitespace."""
    assert text, "entry text must not be empty"
    assert text == text.strip(), "entry text must not have leading/trailing whitespace"
    assert "\n" not in text, "entry text must be a single line"
    assert len(text) <= 280, "entry text must fit in 280 characters"
    return text


def main() -> None:
    """Validate the fortune and write it to /output/entry.txt."""
    validate_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
