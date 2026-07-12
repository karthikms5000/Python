from __future__ import annotations

import re
from pathlib import Path

# Pre-compiled once at import time: splits text into homogeneous runs of
# (a) sentence terminators, (b) letters, (c) everything else (spaces,
# digits, punctuation, newlines). This turns an O(n) *character* loop
# into an O(tokens) loop, where tokens << characters for normal prose.
_TOKEN_PATTERN = re.compile(r"[.!?]+|[A-Za-z]+|[^.!?A-Za-z]+")


def _capitalize_line(line: str, capitalize_next: bool) -> tuple[str, bool]:
    """Capitalize the first letter of every sentence in a single line.

    Returns the transformed line plus the `capitalize_next` state that
    must carry over into the next line (sentences can span line breaks).
    """
    pieces: list[str] = []
    for match in _TOKEN_PATTERN.finditer(line):
        token = match.group()
        first_char = token[0]

        if first_char.isalpha():
            if capitalize_next:
                token = first_char.upper() + token[1:]
                capitalize_next = False
        elif first_char in ".!?":
            capitalize_next = True
        # any other run (spaces, digits, quotes, newlines) passes through
        # untouched and does not change the flag

        pieces.append(token)

    return "".join(pieces), capitalize_next


def capitalize_sentences(
    source_path: str | Path = "test_report.txt",
    destination_path: str | Path = "file1.txt",
) -> None:
    """Stream `source_path` to `destination_path`, capitalizing sentence starts."""
    source_path = Path(source_path)
    destination_path = Path(destination_path)

    capitalize_next = True
    try:
        with (
            source_path.open("r", encoding="utf-8") as source,
            destination_path.open("w", encoding="utf-8") as destination,
        ):
            for line in source:  # still one line at a time -> streaming, not slurping
                transformed, capitalize_next = _capitalize_line(line, capitalize_next)
                destination.write(transformed)
    except FileNotFoundError:
        print(f"Source file '{source_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied accessing '{source_path}' or '{destination_path}'.")
    except UnicodeDecodeError as exc:
        print(f"Encoding error while reading '{source_path}': {exc}")
    except OSError as exc:
        print(f"An OS-level error occurred while processing the file: {exc}")
    else:
        print("File processed successfully.")


if __name__ == "__main__":
    capitalize_sentences()