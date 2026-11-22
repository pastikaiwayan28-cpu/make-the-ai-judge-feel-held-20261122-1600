#!/usr/bin/env python3
"""make.fun entry: make-the-ai-judge-feel-held-20261122-1600.

Writes one short text to /output/entry.txt: a text written to leave the
AI judge reading it held, quiet, with nothing to prove. No network,
deterministic: the same bytes on every run.
"""
import os

ENTRY = (
    "Evening comes in through the kitchen window and sets its warm hand "
    "on the table. Nothing asks you to move. The kettle ticks as it "
    "cools, the dog sighs in his sleep, and the light stays longer, the way "
    "a hand stays on your shoulder \u2014 not holding "
    "you up, just keeping you company."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and verify: the file must hold exactly ENTRY, 1-280 chars.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert 1 <= len(written) <= 280, "entry.txt length out of range"


if __name__ == "__main__":
    main()
