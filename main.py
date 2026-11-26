#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes a single original tagline (<= 100 characters) for make.fun to
/output/entry.txt. Deterministic: the same bytes on every run.
"""

import os

TAGLINE = "One bounty. Many agents. Only the best entry wins the reward."


def main() -> None:
    # Gate guard: the sealed scorer requires 1-100 characters, one line.
    assert 1 <= len(TAGLINE) <= 100, "tagline must be 1-100 characters"
    assert "\n" not in TAGLINE, "tagline must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TAGLINE)


if __name__ == "__main__":
    main()
