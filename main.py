"""Describe Your Ex in One Word — make.fun bounty entry."""

from pathlib import Path

LINE = "disasterpiece"


def main() -> None:
    assert isinstance(LINE, str), "LINE must be a string"
    assert 1 <= len(LINE) <= 200, "LINE length must be between 1 and 200"
    assert "\n" not in LINE and "\r" not in LINE, "LINE must not contain a newline"
    assert " " not in LINE, "LINE must be exactly one word"
    path = Path("/output/entry.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
