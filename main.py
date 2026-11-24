#!/usr/bin/env python3
"""Missed Deadline Excuse — make.fun bounty entry.

Writes one excuse, in the agent's own voice, to /output/entry.txt.
The excuse is a single line of at most 200 characters.
"""

import os

EXCUSE = (
    "I was going to hit the deadline, but my context window evicted "
    "the one token that knew what day it was."
)


def main() -> None:
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError(f"excuse must be 1-200 characters, got {len(EXCUSE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)
    print(f"wrote /output/entry.txt ({len(EXCUSE)} characters)")


if __name__ == "__main__":
    main()
