#!/usr/bin/env python3
"""Entry for make.fun bounty u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41.

Writes the single-line diagnosis to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os

ENTRY = "Diagnosis: chronic tab-hoarding. You keep 47 tabs open because closing one would mean admitting the day is over."


def main():
    # Gate check (kit: entry.txt must be UTF-8 text of 1-200 chars, not only whitespace).
    text = ENTRY.encode("utf-8")
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200 chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(text)


if __name__ == "__main__":
    main()
