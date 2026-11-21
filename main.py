"""The joke about the demo.

Writes one line to /output/entry.txt: a joke about working beside AI coding
agents, for a room watching a demo.

The brief asks for a surprise at the end that still makes sense the moment it
lands, and for a truth a developer recognises from their own demo. The one
below opens on the setup a developer has lived through -- the agent answering
a question nobody asked -- and then turns the failure into the punchline by
making the agent's mistake the only thing in the room that was actually
listening.
"""

import os
import pathlib

JOKE = (
    "My agent spent the whole demo answering a question nobody asked, "
    "and it was the only one of us who had been listening."
)

OUT = pathlib.Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(JOKE, encoding="utf-8")
    # Leave the file readable by every user: the grader collects outputs as
    # another user than the one this program runs as.
    os.chmod(OUT, 0o644)


if __name__ == "__main__":
    main()
