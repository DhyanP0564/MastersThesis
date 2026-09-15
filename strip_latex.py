#!/usr/bin/env python3
"""Strip LaTeX markup down to plain prose text.

Usage:
    python3 strip_latex.py paper.tex                # prints to stdout
    python3 strip_latex.py paper.tex -o paper.txt    # writes to file
    pbpaste | python3 strip_latex.py -               # read from stdin, e.g. clipboard
    python3 strip_latex.py paper.tex | pbcopy        # copy result to clipboard
"""

import argparse
import sys

from pylatexenc.latex2text import LatexNodes2Text


def strip_latex(source: str) -> str:
    text = LatexNodes2Text(math_mode="remove").latex_to_text(source)
    lines = [line.rstrip() for line in text.splitlines()]
    cleaned = []
    blank_run = 0
    for line in lines:
        if line == "":
            blank_run += 1
            if blank_run > 1:
                continue
        else:
            blank_run = 0
        cleaned.append(line)
    return "\n".join(cleaned).strip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Path to .tex file, or '-' for stdin")
    parser.add_argument("-o", "--output", help="Write to this file instead of stdout")
    args = parser.parse_args()

    if args.input == "-":
        source = sys.stdin.read()
    else:
        with open(args.input, "r", encoding="utf-8") as f:
            source = f.read()

    result = strip_latex(source)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()
