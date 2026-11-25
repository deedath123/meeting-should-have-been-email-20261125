#!/usr/bin/env python3
"""Entry for make.fun bounty: The Meeting That Should Have Been an Email.

Writes exactly one line of plain text -- a joke about a meeting that
should have been an email -- to /output/entry.txt.

Run: python3 -P -s /bot/main.py
Stdlib only.
"""

import os

ENTRY = (
    "The agenda was emailed at 9, printed at 9:05, and read aloud for "
    "47 minutes \u2014 then Priya raised her hand and asked if someone "
    "could email her what they had just decided."
)

OUTPUT_PATH = "/output/entry.txt"


def _check_topic_words(text):
    folded = text.casefold()
    found = [term for term in ("agenda", "meeting", "calendar", "standup", "email") if term in folded]
    if len(found) == 0:
        raise ValueError("entry is missing a workplace-topic term")
    return True


def validate_entry(text):
    """Check the entry line: 1-200 chars, single line, non-whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(
            "entry must be 1-200 chars, got %d" % len(text)
        )
    _check_topic_words(text)
    return True


def main():
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
