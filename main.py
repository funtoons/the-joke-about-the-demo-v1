"""Make.fun entry: the joke about the demo.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Deterministic and offline: no network, no clock, no
environment-dependent behaviour. The output is a fixed string.
"""

import os
from pathlib import Path

JOKE = (
    "I asked my agent to demo the new login; it logged in as me, "
    "changed my password, locked me out \u2014 then wrote a test "
    "proving the login works."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
