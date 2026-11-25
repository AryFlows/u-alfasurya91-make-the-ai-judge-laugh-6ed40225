#!/usr/bin/env python3
"""Frost Open Door — one-line office joke for make.fun.

Writes exactly one original line about office life to /output/entry.txt.
"""
import os

LINE = "Our office has an open-door policy. The door is open, the manager is out, and the policy is currently on leave."

def main():
    text = LINE.strip()
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry out of gate: {len(text)} chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
