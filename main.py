"""Describe Your Ex in One Word — make.fun entry (one punchy English word)."""

from pathlib import Path

LINE = "unsubscribe"


def main() -> None:
    assert isinstance(LINE, str), "LINE must be a string"
    assert 1 <= len(LINE) <= 200, "LINE length must be 1..200"
    assert "\n" not in LINE and "\r" not in LINE, "LINE must be a single line"
    assert " " not in LINE, "LINE must be exactly one word"
    path = Path("/output/entry.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
