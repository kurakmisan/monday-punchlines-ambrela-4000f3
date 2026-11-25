"""Monday Morning Punchlines.

Writes a single original joke about Monday mornings to /output/entry.txt
(UTF-8, 1-200 characters). No input, no network, standard library only,
same bytes on every run.
"""

import os

# Candidate Monday-morning jokes drafted for this entry.
# The entry is the line at index PICK; the others stay as the record of the draft.
# Pick rationale (PICK 0): clearly about Monday mornings; a real turn, not a
# complaint - the bed and the boss, two opposing forces, agreeing with each
# other is the surprise; 76 characters, every word doing work; fresh angle
# that avoids the tired coffee / alarm / snooze cliches.
CANDIDATES = [
    "Monday is the only day my bed and my boss agree: I should have stayed in it.",
    "My alarm gave up on Mondays and now just texts my boss: he's awake, emotionally unavailable.",
    "Monday morning: my calendar greets me like a landlord who already knows the rent is late.",
    "I set five alarms for Monday. They unionised and negotiated me down to a single snooze.",
    "Monday asked my weekend for a reference; my weekend said I was excellent at sleeping in and left.",
    "My Monday alarm doesn't ring anymore. It just sighs and asks if we're really doing this again.",
    "Monday is proof my weekend has an evil twin who arrives early, eats my motivation, and bills me for it.",
    "My coffee machine files for overtime every Monday, and my mug is its only witness.",
    "Monday morning is the only meeting my motivation declines without giving a reason.",
    "I told Monday I'd be five minutes late; Monday told my boss I'm five years behind on my life goals.",
]

PICK = 0

MAX_CHARS = 200


def entry_text() -> str:
    line = " ".join(CANDIDATES[PICK].split())
    if not line or len(line) > MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(line)}")
    return line


def main() -> None:
    out_dir = os.environ.get("MONDAY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(entry_text())


if __name__ == "__main__":
    main()
