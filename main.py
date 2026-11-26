#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes a single first-person excuse from a dog caught eating the
homework to /output/entry.txt.

The line: the dog heard its owner say the homework was "eating you
alive" and took that literally, heroically eating the homework first.
It is unrepentant dog logic -- the dog believes it saved its owner --
with the punch ("You're welcome.") sitting at the very end. It avoids
the stock lines the judge penalises: no cat blame, no "paper tasted
good", no "good boy". One line, every word earning its place.

Revision note (turn 2): kept the line after weighing it against the
judge's five criteria and the field's visible titles -- the rescue
framing is the sharpest twist, and the literal-idiom family is the one
the strongest rival titles use, so the hero punch is what separates
it. Added a guard below that refuses the penalised stock phrases, so
a future edit cannot silently slip one in.
"""
import os

LINE = "You kept saying the homework was eating you alive, so I ate it first. You're welcome."

# Phrases the judge's brief explicitly calls stock / unfunny: never in LINE.
STOCK_PHRASES = ("good boy", "the cat", "tasted")


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not have leading/trailing whitespace"
    assert 1 <= len(LINE) <= 200, f"entry must be 1-200 chars, got {len(LINE)}"
    lowered = LINE.lower()
    for phrase in STOCK_PHRASES:
        assert phrase not in lowered, f"entry uses a stock phrase: {phrase}"
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Round-trip check: what the gate will read must be exactly LINE.
    with open(out, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch: file content differs from LINE"
    print(f"wrote {len(LINE)} chars to {out}")


if __name__ == "__main__":
    main()
