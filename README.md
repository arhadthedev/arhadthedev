### Hi 👋

I am **Oleg Iarygin**, a postgrad student of Computer Science who builds up a portfolio
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
`git filter-branch --env-filter "GIT_COMMITTER_DATE=$GIT_AUTHOR_DATE"`.


### Open Source

Contributions into projects I care about (updated weekly by [a GitHub Actions workflow](https://github.com/arhadthedev/arhadthedev/blob/main/.github/workflows/update.yml)):

- Python interpreter:
  - **python/cpython**: [38 already merged commits](https://github.com/python/cpython/commits?author=arhadthedev), [13 PRs are awaiting merging](https://github.com/python/cpython/pulls/arhadthedev), [22 reported issues](https://github.com/python/cpython/issues?q=is%3Aissue+author%3Aarhadthedev)
  - **python/core-workflow**: [2 PRs are awaiting merging](https://github.com/python/core-workflow/pulls/arhadthedev)
  - **python/bedevere**: [1 already merged commit](https://github.com/python/bedevere/commits?author=arhadthedev)
  - **python/devguide**: [2 already merged commits](https://github.com/python/devguide/commits?author=arhadthedev)
  - **python/pyperformance**: [1 already merged commit](https://github.com/python/pyperformance/commits?author=arhadthedev)
  - **sphinx-contrib/sphinx-lint**: [1 already merged commit](https://github.com/sphinx-contrib/sphinx-lint/commits?author=arhadthedev)
  - lots of my comments and reviews [of other's PRs and issues in python/\*](https://github.com/search?q=commenter%3Aarhadthedev+-author%3Aarhadthedev+org%3Apython)

- ECMAScript (aka JavaScript) specification:
  - **tc39/ecma262**: [1 already merged commit](https://github.com/tc39/ecma262/commits?author=arhadthedev), [6 reported issues](https://github.com/tc39/ecma262/issues?q=is%3Aissue+author%3Aarhadthedev)
  - lots of my comments and reviews [of other's PRs and issues in psf/\*](https://github.com/search?q=commenter%3Aarhadthedev+-author%3Aarhadthedev+org%3Atc39)


### GitHub Stats

Generated by [anuraghazra/github-readme-stats](https://github.com/anuraghazra/github-readme-stats):

![Arhadthedev’s GitHub stats](https://github-readme-stats.vercel.app/api?username=arhadthedev&show_icons=true)
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=arhadthedev&layout=compact&exclude_repo=unrealwiki-offline-20080405,uttexture-20140808,beyondunreal-wiki-20161217)


### Useful third party online tools I use

- **GitHub infrastructure**
  - [rhysd/actionlint](https://rhysd.github.io/actionlint/), a static checker for GitHub Actions workflow files
- **Web development**
  - [Live DOM Viewer](https://software.hixie.ch/utilities/js/live-dom-viewer/), a parser of HTML pages for checking if minimization breaks them
- **C/C++ development**
  - [Compiler Explorer](https://gcc.godbolt.org/), an online compiler for checking assembler output of various compilers of various languages
  - [AsmGrid](https://asmjit.com/asmgrid/), a verbose table of Intel/AMD instruction opcodes
  - [ODA Web](https://onlinedisassembler.com/odaweb/), an online disassembler
- **Graphics**
  - [Shadertoy](https://www.shadertoy.com/), a playground for writing and sharing OpenGL/WebGL shaders
- **Entertainment**
  - [magcius/noclip.website](https://github.com/magcius/noclip.website) ([live](https://noclip.website)), a digital museum of video game levels
  - [TIC-80](https://github.com/nesbox/TIC-80) ([live WebAssembly version](https://tic80.com/play)), a fantasy 8-bit game console, games included
  - [Triang3l/WebQuake](https://github.com/Triang3l/WebQuake), a HTML5/WebGL source port of Quake <sub>(was live on webquake.quaddicted.com until 2020)</sub>

### Offline tools

- When CPython developers need to remove some function or class from Python, they do *a code search for foo.bar in PyPI top 5000 projects*. For this, they use the <https://github.com/vstinner/misc/blob/main/cpython/download_pypi_top.py> script.

   <details><summary>More on the tool</summary>

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

   Found at <https://www.mail-archive.com/python-dev@python.org/msg114613.html>.

   </details>
   
### Afterword

[![xkcd Dependency panel (All modern digital infrastructure vs A project some random person in Nebraska has been thanklessly maintaining since 2003)](https://imgs.xkcd.com/comics/dependency.png)](https://xkcd.com/2347/)
