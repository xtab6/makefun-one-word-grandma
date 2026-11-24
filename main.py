#!/usr/bin/env python3
"""One Word From Grandma — a single word, exactly as grandma would say it.

Deterministic, stdlib only, no network, no randomness. Writes the chosen
word to /output/entry.txt and prints it. One word, warm and baffled — the
sound of a grandma meeting new technology for the first time.
"""

import os

WORD = "Witchcraft"


def main():
    os.makedirs("/output", exist_ok=True)
    # A trailing newline keeps the file a well-formed text file; the gate
    # counts 1–30 characters and this word is 10, newline included.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    print(WORD)


if __name__ == "__main__":
    main()
