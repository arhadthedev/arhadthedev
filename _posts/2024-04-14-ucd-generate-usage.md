---
tags: ["rust"]
---

# Automate 

According to crates.io, *ucd-generate* crate is:

> A program for generating packed representations of the Unicode character database that can be efficiently searched.

In other words, it repacks specifies UCD database Unicode code point properties into a `.rs` file as easy-to use arrays. This is tequired to not bring the whole UCD along with our program and to not write file I/O with error management and fallbacks.

However, we need to supply it the latest copy of UCD database. Repetitive manual download may lead to errors so I automated both the download and *ucd-generate* invocation with intended flags.

The result is a CI/CD-friendly script I put as `tools/update_ucd.py` into my Rust repositories that need it:

```python
#!/usr/bin/env python 
"""
Update parser knowledge about character ranges to the latest Unicode version.

Call it on new Unicode release.

This script downloads the UCD (Unicode Character Directory) of the latest
Unicode version and uses it to regenerate src/_tokenizer/unicode_categories.rs.
"""

from pathlib import Path
from tempfile import TemporaryDirectory, TemporaryFile 
from subprocess import check_call, check_output
from urllib.request import urlopen
from zipfile import ZipFile

def download_ucd(output_path: Path):
    packed = urlopen('https://www.unicode.org/Public/zipped/latest/UCD.zip')
    with TemporaryFile() as ucd_archive:
        ucd_archive.write(packed.read())
        with ZipFile(ucd_archive) as ucd_archive_stream:
            ucd_archive_stream.extractall(output_path)


def install_generator():
    check_call("cargo install ucd-generate")


def generate(ucd: Path):
    args = [
        'ucd-generate',
        'general-category', str(ucd),
        '--include', 'Space_Separator',
        '--chars',
        '--enum'
    ]
    generated_content = check_output(' '.join(args), encoding='utf-8')
    repository_root = Path(__file__).parent.parent.resolve()
    out_path = repository_root / 'src' / '_tokenizer' / 'unicode_categories.rs'
    with open(out_path, mode='w') as updated_file:
        updated_file.write(generated_content)

with TemporaryDirectory() as ucd_root_path:
    ucd_root = Path(ucd_root_path)

    print("Downloading UCD...")
    download_ucd(ucd_root)

    print("Installing ucd-generate...")
    install_generator()

    print("Generating tables from UCD...")
    generate(ucd_root)

    print("Updating src/_tokenizer/unicode_categories.rs....")
    regenerate_from_generated(ucd_root)
```
