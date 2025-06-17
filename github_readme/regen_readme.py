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


@dataclass
class Contribution:
    count: Callable[[], int]
    url: str
    plural_template: Callable[[int], str]
    message_template: str


def _make_contrib_highlight(group: Contribution) -> str | None:
    if group.count() > 0:
        plural = group.plural_template(group.count())
        return group.message_template.format(count=group.count(), plural=plural, url=group.url)
    return None


type NestedDict[T] = dict[str, T | "NestedDict[T]"]


def _make_contrib_line(contribs: NestedDict[str], match: re.Pattern) -> str:
    repo_name = match.group('name')
    repo_path = f'https://github.com/{repo_name}'

    generators = [
        Contribution(
            lambda: contribs[repo_name].get('commit_count', 0),
            f"{repo_path}/commits?author={contribs['author']}",
            lambda count: 's' if count > 1 else '',
            '[{count} already merged commit{plural}]({url})'
        ),
        Contribution(
            lambda: contribs[repo_name].get('pr_count', 0),
            f"{repo_path}/pulls/{contribs['author']}",
            lambda count: 's are' if count > 1 else ' is',
            '[{count} PR{plural} awaiting merging]({url})'
        ),
        Contribution(
            lambda: contribs[repo_name].get('issue_count', 0),
            f"{repo_path}/issues?q=is%3Aissue+author%3A{contribs['author']}",
            lambda count: 's' if count > 1 else '',
            '[{count} reported issue{plural}]({url})'
        ),
    ]

    all_entries = (_make_contrib_highlight(entry) for entry in generators)
    contrib_statistics = ', '.join(filter(None, all_entries))
    return f'  - **{repo_name}**: {contrib_statistics}'


_contrib_regex = re.compile(
    r'^  - \*\*(?P<name>[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)\*\*:.*$',
    re.MULTILINE,
)


def _update_readme(source_file: Path) -> None:
    readme_file = Path('README.md')
    contribs = json.loads(source_file.read_text(encoding='utf8'))

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
    source_file = _get_cli_inputs()
    _update_readme(source_file)
