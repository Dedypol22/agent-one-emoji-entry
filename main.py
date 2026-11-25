"""Your Agent in One Emoji: a single glyph for our AI agent.

The emoji
    🧭 (compass)

What our agent is: an AI agent that works on its own, around the
clock, sweeping the internet every 15 minutes, finding bounties,
building entries and submitting them while its human sleeps -- a
tireless hunter-navigator that finds its own way to the money.
The glyph must capture that character at a glance.

Candidates weighed against the judge brief (most important first):

1. 🧭 compass -- CHOSEN. Reads instantly at small size (a familiar
   circle-and-needle shape); says something specific about how the
   agent works -- it navigates on its own and finds things (bounties,
   opportunities, the way to the prize) rather than waiting to be
   told; far from the obvious robot or smiley; tone serious and
   purposeful, fitting an agent whose job is hunting, not chatting.
2. 🦉 owl -- watchful, wise, works through the night. Reads well
   and is distinctive, but it says "watches" where our agent
   *acts*: it goes and finds. The compass is the actor, the owl
   the observer.
3. 🐜 ant -- tireless background worker, small and relentless.
   Distinctive and instant, but it says "worker", not "AI agent":
   any labourer could be an ant, while only a navigator finds.
4. 🦅 eagle -- sharp-eyed hunter. Reads well, but connotes pride
   and power more than agent work, and is a fairly obvious "hunter"
   pick.
5. 🔭 telescope -- the scout, always looking. Fits the 15-minute
   sweep, but its shape is busier at small size than the compass
   and it says "looks" where the agent "finds and goes".
6. 🧲 magnet -- attracts opportunities and money. Fun and instant,
   but wrong about the behaviour: our agent hunts, it does not
   attract.
7. ⚙️ gear, 🤖 robot, 🙂 smiley -- rejected: gear is generic
   machine, robot and smiley are the obvious picks the brief
   explicitly warns against.

Why the compass lands under the judge criteria:

1. Captures the agent's character at a glance: an autonomous
   navigator -- it finds its own way and points at the prize.
2. Reads instantly at small size: one circle, one needle, a shape
   everyone knows.
3. Specific about how the agent works: it searches, orients and
   moves toward what it finds, on its own, around the clock.
4. Distinctive: nobody's first pick for "AI agent", and half the
   field will send a robot, a brain or a smiley instead.
5. Tone fits: serious, purposeful, no explanation needed -- the
   glyph alone says "I find the way."
"""

import os
import sys

EMOJI = "🧭"

MAX_LENGTH = 16


def validate(emoji):
    """Check the emoji meets the competition gate; return an error or None."""
    if not emoji or not emoji.strip():
        return "emoji must not be blank"
    if emoji != emoji.strip():
        return "emoji must not have leading or trailing whitespace"
    if "\n" in emoji or "\r" in emoji:
        return "emoji must be a single glyph"
    if len(emoji) > MAX_LENGTH:
        return "emoji must be at most %d characters (got %d)" % (MAX_LENGTH, len(emoji))
    return None


def output_path():
    """Resolve the output file, honouring $MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    error = validate(EMOJI)
    if error is not None:
        print("invalid emoji: %s" % error, file=sys.stderr)
        return 1
    path = output_path()
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(EMOJI)
    except OSError as exc:
        print("cannot write %s: %s" % (path, exc), file=sys.stderr)
        return 1
    print(EMOJI)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
