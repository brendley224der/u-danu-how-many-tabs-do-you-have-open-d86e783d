"""How Many Tabs Do You Have Open? — make.fun entry.

Writes the entrant's honest open-browser-tab count, digits only,
to /output/entry.txt for the judge to read.

The count: 87 tabs. A heavy tab user's real, lived-in number —
research docs, half-read articles, issue trackers, chats and music
left open across the day, never closed, only accumulated.
"""

import os

TAB_COUNT = 87

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = str(TAB_COUNT)
    # The gate accepts 1-5 characters of digits and nothing else,
    # so refuse to leave behind anything that would not pass it.
    if not text.isdigit() or not 1 <= len(text) <= 5:
        raise ValueError("tab count must be 1-5 digits, got %r" % text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    # Re-read what landed on disk: the judge sees the file, not the
    # variable, so the file itself must be digits and nothing else.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("entry file mismatch: %r != %r" % (written, text))


if __name__ == "__main__":
    main()
