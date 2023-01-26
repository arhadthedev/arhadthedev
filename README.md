### Hi 👋

I am **Oleg Iarygin**, a master of Computer Science who builds up a portfolio
here and resolves use case pains in other projects. Also I have a miraculous
ability to use stuff in unintended ways without being aware of it, so I
constantly meet lags and crashes.

- 🔭 I’m currently working on a web browser that doesn’t freeze as heavy as
Chromium on my 4GB RAM 500GB HDD *work*station.
- 🌱 I’m currently learning low-level NT API because classical Windows network
API is partially synchronous and has thick multilayer wrappers for
compatibility I don’t need. However, this knowledge has no use if the
application is for Windows Store.
- 👯 I’m looking to collaborate on C or C++ desktop or network backend projects.
- 💬 Ask me about mitigation of C qirks, how to port a static site to an ad-hoc
Python generator, and how to preserve sanity in the process.
- 📫 How to reach me:
  oleg@arhadthedev.net,
  [Twitter](https://twitter.com/arhadthedev),
  [VK](https://vk.com/arhadthedev) (the PM is open for everyone).
- 😄 Pronouns: He/Him.
- ⚡ Fun fact: I’m a fan of Unreal Gold.

🧼 Pro tip: keep hands sanitized after each rebase with
<code>git filter-branch --env-filter "GIT_COMMITTER_DATE=$GIT_AUTHOR_DATE" HEAD~*howmanycommits*..HEAD</code>.


### Open Source

Contributions into projects I care about (updated weekly by [a GitHub Actions workflow](https://github.com/arhadthedev/arhadthedev/blob/main/.github/workflows/update.yml)):

- Python interpreter:
  - **python/cpython**: [45 already merged commits](https://github.com/python/cpython/commits?author=arhadthedev), [10 PRs are awaiting merging](https://github.com/python/cpython/pulls/arhadthedev), [22 reported issues](https://github.com/python/cpython/issues?q=is%3Aissue+author%3Aarhadthedev)
  - **python/core-workflow**: [1 already merged commit](https://github.com/python/core-workflow/commits?author=arhadthedev), [1 PR is awaiting merging](https://github.com/python/core-workflow/pulls/arhadthedev)
  - **python/bedevere**: [1 already merged commit](https://github.com/python/bedevere/commits?author=arhadthedev)
  - **python/devguide**: [2 already merged commits](https://github.com/python/devguide/commits?author=arhadthedev), [1 reported issue](https://github.com/python/devguide/issues?q=is%3Aissue+author%3Aarhadthedev)
  - **python/pyperformance**: [1 already merged commit](https://github.com/python/pyperformance/commits?author=arhadthedev)
  - **sphinx-contrib/sphinx-lint**: [1 already merged commit](https://github.com/sphinx-contrib/sphinx-lint/commits?author=arhadthedev)
  - lots of my comments and reviews [of other's PRs and issues in python/\*](https://github.com/search?q=commenter%3Aarhadthedev+-author%3Aarhadthedev+org%3Apython)

- ECMAScript (aka JavaScript) specification:
  - **tc39/ecma262**: [1 already merged commit](https://github.com/tc39/ecma262/commits?author=arhadthedev), [6 reported issues](https://github.com/tc39/ecma262/issues?q=is%3Aissue+author%3Aarhadthedev)
  - lots of my comments and reviews [of other's PRs and issues in psf/\*](https://github.com/search?q=commenter%3Aarhadthedev+-author%3Aarhadthedev+org%3Atc39)

I also randomly contribute to any repository I use in my code: [issues](https://github.com/search?p=1&q=author%3Aarhadthedev+-org%3Apython+-org%3Atc39+-org%3Aarhadthedev+is%3Aissue), [PRs](https://github.com/search?q=author%3Aarhadthedev+-org%3Apython+-org%3Atc39+-org%3Aarhadthedev+is%3Apr), and [comments](https://github.com/search?q=commenter%3Aarhadthedev+-author%3Aarhadthedev+-org%3Apython+-org%3Atc39+-org%3Aarhadthedev).


### GitHub Stats

Generated by [anuraghazra/github-readme-stats](https://github.com/anuraghazra/github-readme-stats):

![Arhadthedev’s GitHub stats](github-readme-stats.zohan.tech)
![Top Langs](github-readme-stats.zohan.tech/api/top-langs/?username=arhadthedev&layout=compact&exclude_repo=qt-4.3.5,unrealwiki-offline-20080405,uttexture-20140808,beyondunreal-wiki-20161217)


### Useful third party online tools I use

- **GitHub infrastructure**
  - [actionlint](https://rhysd.github.io/actionlint/) ([sources](https://github.com/rhysd/actionlint)), a static checker for GitHub Actions workflow files
- **Web development**
  - [Live DOM Viewer](https://software.hixie.ch/utilities/js/live-dom-viewer/), a parser of HTML pages for checking if minimization breaks them
- **C/C++ development**
  - [Compiler Explorer](https://gcc.godbolt.org/) ([sources](https://github.com/compiler-explorer/compiler-explorer)), an online compiler for checking assembler output of various compilers of various languages
  - [AsmGrid](https://asmjit.com/asmgrid/), a verbose table of Intel/AMD instruction opcodes
  - [ODA Web](https://onlinedisassembler.com/odaweb/), an online disassembler
- **Graphics**
  - [Shadertoy](https://www.shadertoy.com/), a playground for writing and sharing OpenGL/WebGL shaders
- **Entertainment**
  - [noclip.website](https://noclip.website) ([sources](https://github.com/magcius/noclip.website)), a digital museum of video game levels
  - [TIC-80](https://tic80.com/play) ([sources of a desktop version](https://github.com/nesbox/TIC-80)), a fantasy 8-bit game console, games included
  - WebQuake ([sources](https://github.com/Triang3l/WebQuake)), a HTML5/WebGL source port of Quake <sub>(was live on webquake.quaddicted.com until 2020)</sub>
- **Maintenance**
  - [endoflife.date](https://endoflife.date/) ([sources](https://github.com/endoflife-date/endoflife.date)), a centralized list of per-version support status for 136 popular programs, services and OSes

### Offline tools

- When CPython developers need to remove some function or class from Python, they do *a code search for foo.bar in PyPI top 5000 projects*. For this, they use [`download_pypi_top.py`](https://github.com/vstinner/misc/blob/main/cpython/download_pypi_top.py) and [`search_pypi_top.py`](https://github.com/vstinner/misc/blob/main/cpython/search_pypi_top.py) scripts by Victor Stinner.

   <details><summary>More on the tools</summary>

   ```text
   $ python download_pypi_top.py --help

   usage: download_pypi_top.py [-h] DIRECTORY [COUNT]

   Download the source code of PyPI top projects.

   positional arguments:
     DIRECTORY   Destination directory
     COUNT       Only download the top COUNT projects

   options:
     -h, --help  show this help message and exit
   ```

   Discovered via <https://www.mail-archive.com/python-dev@python.org/msg114613.html>.
  
   ```text
   usage: search_pypi_top.py [-h] [-o FILENAME] [--text] [-v] [-q] [--cython]
                             PYPI_DIRECTORY REGEX

   Code search in the source code of PyPI top projects.

   positional arguments:
     PYPI_DIRECTORY        PyPI local directory
     REGEX                 Regex to search

   options:
     -h, --help            show this help message and exit
     -o FILENAME, --output FILENAME
                        Output filename
     --text                Process a binary file as if it were text
     -v, --verbose         Verbose mode (ex: log ignored files)
     -q, --quiet           Quiet mode (ex: don't log proceed files)
     --cython              Search also in code generated by Cython
   ```

   Discovered via <https://github.com/python/cpython/pull/99285#pullrequestreview-1186015484>.

   </details>
   
### Afterword

[![xkcd Dependency panel (All modern digital infrastructure vs A project some random person in Nebraska has been thanklessly maintaining since 2003)](https://imgs.xkcd.com/comics/dependency.png)](https://xkcd.com/2347/)
