#!/usr/bin/env python3
"""Last Text at One Percent -- make.fun entry (program/v1).

Writes the dying phone's final text message to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

import os

ENTRY = "Before I die: I cancelled your 7am alarm. Sleep in. Bring a charger next time."
# Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not only
# whitespace. This entry is 78 characters: short, punchy, one text and nothing else.

def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
