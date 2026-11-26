"""Write the entry word for make.fun's "One Word From Grandma" bounty.

Exactly one word, at most 30 characters: the word a grandma would text
about AI. The program writes the word to entry.txt under the output
directory and nothing else, so two runs leave byte-identical files. It
uses only the standard library and never touches the network.
"""

import os
import sys
from pathlib import Path

WORD = "Witchcraft"

MIN_CHARS = 1
MAX_CHARS = 30


def write_entry() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = output_dir / "entry.txt"
    if not MIN_CHARS <= len(WORD) <= MAX_CHARS:
        sys.exit("word must be 1 to 30 characters")
    if WORD.split() != [WORD]:
        sys.exit("entry must be exactly one word")
    output_dir.mkdir(parents=True, exist_ok=True)
    # Do not chmod the output directory: the grader runs this program
    # as a different user on a directory it does not own, and chmod
    # would raise PermissionError and fail the run.
    target.write_text(WORD, encoding="utf-8")
    try:
        target.chmod(0o644)
    except PermissionError:
        pass
    return target


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {written} ({len(WORD)} characters, one word)")
