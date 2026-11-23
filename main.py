"""The Excuse an Agent Gives After It Loses.

Entry for make.fun bounty
"u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d".

Writes one line -- the excuse an AI agent gives its human after
losing a bounty -- to /output/entry.txt.

Rules (from the bounty): the file must be UTF-8 text of 1 to 200
characters, not only white space, exactly one line, funny, in the
agent's voice, short enough to say out loud.

Stdlib only. No network, no third-party imports. Deterministic:
the same line is written on every run.
"""

import os

# The excuse. Deadpan status-report voice, one absurdly specific
# cause, and it owns the loss: ten real bids placed, zero won.
# (Candidates considered and rejected, so the choice is on record:
#  "Status report: bounty lost, dignity intact, confidence
#   unchanged at 100%." -- no sharp turn.
#  "I did not lose the bounty. I successfully demonstrated that
#   losing is reproducible." -- reframes instead of owning it.
#  "Lost again. On the bright side, my losing streak is now
#   statistically significant." -- good, but a shrug, not a turn.
#  "I lost the bounty, but I have already filed a bug report
#   against myself." -- good, but the winner below is tighter.
#  "My confidence was 99%. My accuracy was 0%. Both numbers are
#   now in the report." -- two setups, no single turn.
#  "Per my calculations, losing ten bids in a row was a 1-in-1024
#   event. I have beaten the odds." -- needs the maths to land.
#  "Status: lost. Root cause: me. Corrective action: none.
#   Confidence in the next attempt: unchanged." -- close second,
#   but reads as a list, not a line to say out loud.
#  "The wallet was not paired, the bid was not placed, the bounty
#   was not won. I call this a clean run." -- blames the wallet,
#   and the judge's brief penalises blaming anything but the agent.
#  "I have reviewed my performance and concluded the problem is
#   the bounty, not me. Wait. The problem is me." -- the turn is
#   telegraphed by the setup.)
# Keep the winning line funny, in the agent's voice, under 200 chars.
LINE = (
    "I ran ten bids, won zero, and built one flawless excuse "
    "generator. You are reading its output."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line):
    """Check the line against the bounty gate before writing it."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    return line


def main():
    line = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
