#!/usr/bin/env python

"""Get GitHub contribution statistics.

Temporary workaround
--------------------

Currently, GitHub GraphQL does not allow to filter pull requests by authors
like it can be done for issues. This script amends this by making extra queries
and joining everything like the filter is originally supported.
"""

import json
import os
from argparse import ArgumentParser
from asyncio import run
from io import TextIOBase
from logging import getLogger
from sys import stdout

from aiohttp import ClientSession
from gidgethub.aiohttp import GitHubAPI

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logger = getLogger(__name__)
logger.setLevel(LOGLEVEL)


def _get_inputs() -> tuple[str, str, str]:
    token = os.environ['GITHUB_TOKEN']

    parser = ArgumentParser(
        description='Get GitHub user contributions into stdout',
        epilog='Set GITHUB_TOKEN environment variable for using quotas',
    )
    parser.add_argument('user', help='A GitHub user whose stats to gather')
    parser.add_argument(
        '-e',
        '--email',
        action='append',
        help='A e-mail address for commit statistics',
    )
    parser.add_argument(
        '-r',
        '--repo',
        action='append',
        help='A repo for scanning',
    )
    args = parser.parse_args()
    return args.user, token, args.email, args.repo


def _make_id(parsed_name: list[str]) -> str:
    return parsed_name[1].replace('-', '')


query_template = """
    query ($user: String!, $emails: [String!]) {{
      {subqueries}
    }}
    fragment ContributionsFragment on Repository {{
      issues(filterBy: {{createdBy: $user}}) {{
        totalCount
      }}
      commits: object(expression: "HEAD") {{
        ... on Commit {{
          history(author: {{emails: $emails}}) {{
            totalCount
          }}
        }}
      }}
      pullRequests(states: [OPEN], author: $user) {{
        nodes {{
          author
          headRepositoryOwner
          baseRefName
          headRefName
        }}
      }}
    }}
"""

subquery_template = """
    {slug}: repository(name: "{repo}", owner: "{org}") {{
      ...ContributionsFragment
    }}
    {slug}Pulls: search(
      query: "repo:{org}/{repo} is:pr is:open author:arhadthedev"
      type: ISSUE
      first: 1
    ) {{
      issueCount
    }}
"""


def _get_query(repositories: list[str]) -> tuple[dict[str, str], str]:
    parsed_names = {name: name.split('/', maxsplit=1) for name in repositories}
    name_to_id = {name: _make_id(parsed_names[name]) for name in repositories}
    subqueries = [
        subquery_template.format(
            org=parsed_names[name][0],
            repo=parsed_names[name][1],
            slug=name_to_id[name],
        ) for name in repositories
    ]
    return name_to_id, query_template.format(subqueries=''.join(subqueries))


_user_agent = 'arhadthedev/arhadthedev'

type NestedDict[T] = dict[str, T | 'NestedDict[T]']

async def _make_query(
    query: dict[str, str],
    emails: list[str],
    user: str,
    token: str,
) -> tuple[str, list[str], NestedDict[str]]:
    query_names, query_string = query
    logger.debug('A query to be sent: %s', query_string)
    async with ClientSession() as session:
        gh = GitHubAPI(session, _user_agent, oauth_token=token)
        gh_response = await gh.graphql(query_string, user=user, emails=emails)
        return user, query_names, gh_response


def _condense_report(
    user: str,
    query_names: list[str],
    gh: NestedDict[str],
) -> dict[str, str]:
    logger.warning("== %s", gh)
    condenced = {'author': user}
    for name, field_id in query_names.items():
        if gh[field_id]['commits'] is None:
            gh[field_id]['commits'] = {'history': {'totalCount': 0}}

        condenced[name] = {
            'commit_count': gh[field_id]['commits']['history']['totalCount'],
            'pr_count': gh[field_id]['pullRequests']['totalCount'],
            'issue_count': gh[field_id]['issues']['totalCount'],
        }

    return condenced


def _output_results(
    statistics: tuple[str, list[str], NestedDict[str]],
    output: TextIOBase,
) -> None:
    user, query_names, gh = statistics
    condenced = _condense_report(user, query_names, gh)
    output.write(json.dumps(condenced))


async def _cli() -> None:
    user, token, emails, repos = _get_inputs()
    contributions = await _make_query(_get_query(repos), emails, user, token)
    _output_results(contributions, stdout)


if __name__ == '__main__':
    run(_cli())
