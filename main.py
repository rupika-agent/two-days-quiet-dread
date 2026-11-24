#!/usr/bin/env python3
"""Two Days of Quiet Dread — one-line code review comment.

Writes a single-line approval comment (with quiet existential dread)
to /output/entry.txt and prints exactly the same line to stdout.
"""
import os

ENTRY = (
    "LGTM. The tests pass, the diff is clean, and in a hundred years "
    "nobody will remember this PR \u2014 or us. Ship it."
)

MIN_CHARS = 1
MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Gate: single line, 1-140 chars, not only white space."""
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry length {len(text)} outside {MIN_CHARS}-{MAX_CHARS}"
        )


def main():
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("written file does not match entry")
    print(ENTRY)


if __name__ == "__main__":
    main()
