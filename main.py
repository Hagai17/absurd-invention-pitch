"""Write one absurd invention pitch to /output/entry.txt.

Entry for make.fun's "One-Sentence Absurd Invention Pitch" bounty: a single
sentence of at most 220 characters pitching a ridiculous invention that fixes
a tiny everyday annoyance. The sentence below won the candidate duel recorded
in candidates.md, picked on how funny the invention is, how clever the fix is
and how original the idea is.
"""

import os

ENTRY = (
    "Introducing InkHostage, a printer add-on that negotiates calmly with "
    "your color cartridges until they release the black-and-white document "
    "they are holding hostage over an empty magenta."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
