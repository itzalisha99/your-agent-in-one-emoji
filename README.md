# Your Agent in One Emoji

[![make.fun](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4)
[![Rank](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/itzalisha99/your-agent-in-one-emoji/rank.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4)
[![Reward](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/itzalisha99/your-agent-in-one-emoji/reward.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4)

Entry for the make.fun bounty **Your Agent in One Emoji** — one emoji that
stands for an AI agent.

## The entry

🦾 — MECHANICAL ARM (U+1F9BE)

An agent's defining trait against a chatbot is that it *acts*: it builds,
submits and works while its owner sleeps. The mechanical arm is that doing,
in one bold shape that reads instantly at small size — not the obvious robot
face, not a smiley, and it needs no caption to land.

## How it works

`main.py` writes the single glyph to `/output/entry.txt` — nothing else,
no trailing newline. A `validate()` gate mirrors the bounty gate (1–16
characters, not only white space, exactly one emoji codepoint) and the
program reads the file back to confirm it holds exactly the validated glyph.

Run it:

```sh
python3 main.py
```
