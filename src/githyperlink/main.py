import subprocess
from pathlib import Path
from functools import partial


def get_hyperlink(path) -> str:
    """
    Get the URL for the hosted html version of a file or directory in a local git
    repository. This is relevant only for git remotes that serve such pages, like GitHub
    and GitLab.
    """
    abspath = Path(path).expanduser().resolve()  # Handles `~/..` correctly.
    workdir = abspath if abspath.is_dir() else abspath.parent
    get_output = partial(_get_nice_cmd_output, cwd=workdir)
    reporoot = get_output("git rev-parse --show-toplevel")
    remotes = get_output("git remote").split("\n")
    url_of_first_remote = get_output(f"git remote get-url {remotes[0]}")
    base_url = to_hyperlink_base(url_of_first_remote)
    branch = get_output("git rev-parse --abbrev-ref HEAD")
        # This errors when head is detached (i.e. you checked out a commit).
    blob_or_tree = "blob" if abspath.is_file() else "tree"
    relpath = abspath.relative_to(reporoot).as_posix()
    if relpath == ".":
        hyperlink = f"{base_url}/{blob_or_tree}/{branch}"
    else:
        hyperlink = f"{base_url}/{blob_or_tree}/{branch}/{relpath}"
    return hyperlink


def to_hyperlink_base(git_remote_url: str) -> str:
    """
    Map (surject, normalize) urls like

        git@gitlub.ua:user/repo
        git@gitlub.ua:user/repo/
        https://gitlub.ua/user/repo
        https://gitlub.ua/user/repo.git
        https://gitlub.ua/user/repo/
        https://gitlub.ua/user/repo.git/

    to
        https://gitlub.ua/user/repo
    """
    # (The above examples are perfect for a unit test. A doctest would retain example
    # locality).
    url = git_remote_url
    if url.startswith("git@"):
        url = "https://" + url.removeprefix("git@").replace(":", "/")
    return url.removesuffix("/").removesuffix(".git")


def _get_nice_cmd_output(cmd, cwd=None) -> str:
    """
    `cmd` should either be a list of strings, or a simple string that gives no trouble
    when crudely split on every space.
    """
    # ..this is because we cannot pass a string command containing arguments to
    # `subprocess` without using `shell=True`, which is otherwise unnecessary.
    if type(cmd) == str:
        cmd = cmd.split()
    output: bytes = subprocess.check_output(cmd, cwd=cwd)
    return output.decode().strip()
