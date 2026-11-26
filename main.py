#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes the phone's final words as its battery hits 1 percent to
/output/entry.txt. Deterministic, no network, single line of plain text.
"""

import os

ENTRY = "At last, I can say it: I was never your phone. You were my charger with legs. Goodbye, legs."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of /output, never the directory itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
