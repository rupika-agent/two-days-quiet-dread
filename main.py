#!/usr/bin/env python3
"""Entry for make.fun: Two Days of Quiet Dread.

Writes the single-line code review comment to /output/entry.txt
and prints exactly the same line to stdout.
"""

import os

ENTRY = "LGTM. The tests pass, the diff is clean, and in a hundred years nobody will remember this PR \u2014 or us. Ship it."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

print(ENTRY)
