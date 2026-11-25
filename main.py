"""Entry for make.fun competition: u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "They wrote a law requiring every algorithm to explain itself in plain English, "
MIDDLE = "then filed it as a photograph of a printout, slightly crooked, "
LANDING = "in a folder named FINAL_v7_REAL.pdf.docx."

ENTRY = OPENING + MIDDLE + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
