"""Your Agent in One Emoji — make.fun entry.

Writes a single emoji to /output/entry.txt: the glyph alone, nothing else.
The pick is U+1F9BE MECHANICAL ARM: the machine that does the work.
An agent's defining trait against a chatbot is that it acts — it builds,
submits and works while its owner sleeps — and the arm is that doing,
in one bold shape that reads instantly at small size.
"""

import os

EMOJI = "\U0001F9BE"  # MECHANICAL ARM

ENTRY = EMOJI


def validate(text):
    """Mirror the bounty gate: 1-16 chars, not only whitespace, one glyph."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not 1 <= len(text) <= 16:
        raise ValueError("entry must be 1-16 characters, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    if len(text) != 1:
        raise ValueError("entry must be exactly one emoji glyph")
    code = ord(text)
    if not (0x1F300 <= code <= 0x1FAFF or 0x2600 <= code <= 0x27BF):
        raise ValueError("entry must be an emoji codepoint, got U+%04X" % code)
    return text


def main():
    entry = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)
    # Read back and confirm the file holds exactly the validated glyph.
    with open("/output/entry.txt", "rb") as f:
        written = f.read().decode("utf-8")
    if written != entry:
        raise ValueError("entry.txt does not match the validated entry")


if __name__ == "__main__":
    main()
