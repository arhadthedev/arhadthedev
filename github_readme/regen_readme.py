#!/usr/bin/env python

"""Regenerate Open Source section of README.md using prepared statistics.

The statistics are supplied by a JSON file with a dictionary:

.. code-block:: json

    {
        "author": "<a GitHub username of a user that the file describes>",
        "<repo-org/repo-name>": {
            "commit_count": <number>,
            "open_pr_count": <number>,
            "issue_count": <number>
        }
    }
"""

import json
import re
from argparse import ArgumentParser
from collections.abc import Callable
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from typing import Any


@dataclass
class Contribution:
    """Info on one contribution type into one repo."""

    count: Callable[[], int]
    url: str
    message_template: str


def _make_contrib_highlight(group: Contribution) -> str | None:
    if group.count() > 0:
        plural = re.sub(
            r'\((?:([^/]+)/)?([^)]+)\)', # covers both `(is/are)` and `(s)`
            r'\1' if group.count() == 1 else r'\2',
            group.message_template,
        )
        markup = f'[{plural}]({group.url})'
        return markup.format(count=group.count())
    return None


# <https://github.com/python/typeshed/blob/ecd5141c/stdlib/json/__init__.pyi#L50-L60>
# declares `json.load` returning Any so we declate `contribs` as Any too.
def _make_contrib_line(contribs: Any, match: re.Match) -> str:
    repo_name = match.group('name')
    repo_path = f'https://github.com/{repo_name}'

    generators = [
        Contribution(
            lambda: contribs[repo_name].get('commit_count', 0),
            f"{repo_path}/commits?author={contribs['author']}",
            '{count} already merged commit(s)',
        ),
        Contribution(
            lambda: contribs[repo_name].get('pr_count', 0),
            f"{repo_path}/pulls/{contribs['author']}",
            '{count} PR( is/s are) awaiting merging',
        ),
        Contribution(
            lambda: contribs[repo_name].get('issue_count', 0),
            f"{repo_path}/issues?q=is%3Aissue+author%3A{contribs['author']}",
            '{count} reported issue(s)',
        ),
    ]

    all_entries = (_make_contrib_highlight(entry) for entry in generators)
    contrib_statistics = ', '.join(filter(None, all_entries))
    return f'  - **{repo_name}**: {contrib_statistics}'


_contrib_regex = re.compile(
    r'^  - \*\*(?P<name>[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)\*\*:.*$',
    re.MULTILINE,
)


def _update_readme(config_file: Path, readme_file: Path) -> None:
    contribs = json.loads(config_file.read_text(encoding='utf8'))

    line_updater = partial(_make_contrib_line, contribs)
    original_readme = readme_file.read_text(encoding='utf8')
    updated_readme = _contrib_regex.sub(line_updater, original_readme)
    readme_file.write_text(updated_readme, encoding='utf8')


def _get_cli_inputs() -> Path:
    parser = ArgumentParser(description='Regenerate README.md.')
    parser.add_argument(
        'source',
        type=Path,
        help='Path to a JSON file with actual source data.',
    )
    args = parser.parse_args()
    return args.source


if __name__ == '__main__':
    config_file = _get_cli_inputs()
    _update_readme(config_file, Path('README.md'))
