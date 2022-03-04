# githyperlink

Get a link to the web version of a git-tracked file or directory.

Applies to GitHub and GitLab remotes (and maybe others but those are not tested).


## Usage

```bash
$ gethyperlink [PATH]
```
(Note the spelling here: _get_ hyperlink).

If `PATH` is not specified, a link for the current directory is given.

### Example

```bash
$ cd my-pretty-repo/subdir

$ gethyperlink somefile.jl
https://github.com/yourname/my-pretty-repo/blob/main/subdir/somefile.jl
```

You might want to define an alias, for example, in `~/.bashrc`:
```bash
alias gl="gethyperlink"  # Or maybe 'gurl' (get url) 💅
```

### Direct usage in Python

```py
from githyperlink import get_hyperlink

print(get_hyperlink(__file__))
# → https://gitlab.com/you/my_scripts/blob/main/this_script.py
```
The argument to `get_hyperlink` can be a string, as above, or a `pathlib.Path`.


## Installation

```
pip install githyperlink
```
This will get you the

[![Latest release on PyPI](https://img.shields.io/pypi/v/githyperlink.svg?label=latest%20release%20on%20PyPI:)](https://pypi.python.org/pypi/githyperlink/),

and makes the command-line tool `gethyperlink` globally available.

To upgrade an existing installation to the version above, use `pip install -U githyperlink`.

Requires Python ≥ 3.9.


## Features

 - `git` is called directly, in a subprocess: this is faster than the default usage of
   `GitPython`, and spares a dependency. (Currently, we only depend on [`click`](https://click.palletsprojects.com/)).
 
 - Not many features.  
   This makes the source code easier to grok, and easier to modify for your own purposes.
