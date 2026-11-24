"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes one line (at most 140 characters): the funniest excuse a robot
vacuum could offer for missing a spot, in the vacuum's own voice.
"""

import os


ENTRY = (
    "The dust was there, I saw it, but my map says that corner "
    "belongs to the cat now. I do not argue with the cat."
)


def validate_entry(text):
    """Gate: UTF-8 text, 1 to 140 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > 140:
        raise ValueError("entry is over 140 characters: %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    return True


def output_path():
    """Absolute grader output path only: the grader's filesystem is
    read-only except /output, so a relative path would crash."""
    return os.path.join(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output",
        "entry.txt",
    )


def main():
    validate_entry(ENTRY)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %d chars to %s" % (len(ENTRY), path))


if __name__ == "__main__":
    main()
