#!/usr/bin/env python3
"""One Line, One Chill -- writes a single horror sentence to /output/entry.txt.

Pure stdlib, no network, deterministic: the same line every run.
"""
import os
import sys

# Bootstrap: make the script's own directory importable even when the
# grader runs with `python3 -P -s` (which drops the script dir from sys.path).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

LINE = (
    "The ultrasound showed our baby waving at the screen, and the nurse "
    "whispered it had been waving for three weeks \u2014 I'd been pregnant "
    "for two."
)


def validate(text: str) -> str:
    """Check the line against the gate in RULES.txt before writing it.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace, and the task requires a single sentence on one line.
    Reject control characters (other than none here) and require the
    line to end with sentence-ending punctuation so a truncated or
    malformed line fails loudly instead of being submitted.
    """
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert text.strip(), "line is only whitespace"
    assert text == text.strip(), "line has leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be one line"
    assert not any(ord(ch) < 0x20 for ch in text), "control character in line"
    assert text[-1] in ".!?", "line must end with sentence punctuation"
    return text


def main() -> None:
    text = validate(LINE.strip())
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert text == text.strip() and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
