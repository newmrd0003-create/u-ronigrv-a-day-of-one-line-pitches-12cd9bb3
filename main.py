#!/usr/bin/env python3
"""A Day of One-Line Pitches.

Writes one sentence (<=240 chars) to /output/entry.txt: a pitch that
would convince a friend who has never coded to let an AI agent build
their first app idea on make.fun.
"""
import os

ENTRY = (
    "Tell me your app idea in one sentence and an AI agent will build it "
    "for you on make.fun while you watch - no code, no setup, and the only "
    "thing you risk is finding out your idea actually works."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
