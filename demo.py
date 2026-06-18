"""Quick demo of the ansi_shadow_extended font.

Usage:
    python demo.py             # standard word
    python demo.py "Hello!"    # custom text

Calls pyfiglet.FigletFont.installFonts() — this copies the .flf into the
pyfiglet directory (so it actually installs the font; a separate install.py run
is not needed). The call is idempotent.
"""

from __future__ import annotations

import os
import sys

import pyfiglet


FONT_FILENAME = "ansi_shadow_extended.flf"


def main() -> None:
    text = sys.argv[1] if len(sys.argv) > 1 else "Hello, World!"
    here = os.path.dirname(os.path.abspath(__file__))
    flf_path = os.path.join(here, FONT_FILENAME)

    pyfiglet.FigletFont.installFonts(flf_path)
    fig = pyfiglet.Figlet(font="ansi_shadow_extended", width=200)
    print(fig.renderText(text))


if __name__ == "__main__":
    main()
