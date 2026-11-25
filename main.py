"""Make the AI Judge Laugh — entry program.

Writes one office-life joke, a single line under 200 characters, to
/output/entry.txt, exactly as the competition gate requires (UTF-8 text,
1 to 200 characters, not only whitespace).
"""

import os

# The winning one-liner, chosen by manual ranking against the kit's judge
# brief (office-life truth first, surprising last word, tight, original).
# See candidates.md for the full candidate list and ranking.
JOKE = "I asked IT for a second monitor and got a lecture on gratitude, a ticket number, and a chair with one wheel missing."


def main() -> None:
    # Gate self-check (mirrors the sealed scorer): UTF-8, 1-200 chars,
    # single line, not only whitespace. Fail loudly instead of writing
    # an entry the gate would refuse.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly the joke, byte for byte.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
