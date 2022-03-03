import sys
import subprocess
from click import command, argument
from .main import get_hyperlink

@command()
@argument("path", required=False)
def get_and_print_hyperlink(path=None):
    if path is None:
        path = "."
    try:
        url = get_hyperlink(path)
    except subprocess.CalledProcessError:
        # `git` error is already printed to stderr. (Most likely error: not a git repo).
        sys.exit(1)  # So, just quit.
    else:
        print(url)
