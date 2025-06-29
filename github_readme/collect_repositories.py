#!/usr/bin/env python

"""Retrieve repositories I contribute into, mentioned in the README.

To update the contribution statistics in the Open Source Contributions section
of README.md, we need to extract the entries to update.

By the way, regen_readme.py does the very same parsing. We could merge this
script file with that one if not collect_contribs.py called inbetween.
"""

import re
from argparse import ArgumentParser
from pathlib import Path

_contrib_regex = re.compile(
    r'^  - \*\*(?P<name>[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)\*\*:.*$',
    re.MULTILINE,
)


def _extract_repository_names(readme_file: Path) -> list[str]:
    readme = readme_file.read_text(encoding='utf8')
    return [line.group('name') for line in _contrib_regex.finditer(readme)]


def _get_cli_inputs() -> None:
    parser = ArgumentParser(description='Scan README.md for repository names.')
    parser.parse_args()


if __name__ == '__main__':
    _get_cli_inputs()
    names = _extract_repository_names(Path('README.md'))
    print(*names, sep='\n', end='') # noqa: T201 # This is normal console output
