import os
import subprocess
import sys
from importlib import import_module
from pathlib import Path
from types import ModuleType

import click

from . import verbosity as v


def get_glide_root() -> None | Path:
    """Get the GLIDE_ROOT and return it as pathlib.Path (None if not found.)"""

    glide_root = os.environ.get('GLIDE_ROOT')
    if not glide_root:
        click.secho(
            'Missing GLIDE_ROOT environment variable',
            fg='red',
            bold=True,
            err=True)
        click.secho(
            "Set GLIDE_ROOT environment to the top of your assets.",
            err=True)
        return

    if v.verbosity >= 3:
        click.secho(f"glide_root={glide_root}", dim=True)
    return Path(glide_root)


def get_nearest_glideconf(
        glide_root: Path, start_at: None | Path = None) -> tuple[Path, ModuleType]:
    """Starting at start_at, return the nearest glideconf.

    This needs to know the glide root, so it knows what prefix to remove,
    so that dotted paths can work.
    """

    # Don't litter the entire tree upward with __pycache__ junk
    sys.dont_write_bytecode = True

    curr: Path = start_at or Path().cwd()
    asset_path = curr

    # glide_root = /Users/joel/curric/
    # cwd = /Users/joel/curric/lectures/js-oo/demo
    # dotted_path will be = "curric.lectures.js-oo"
    while True:
        if (curr / "glideconf.py").exists():
            break
        curr = curr.parent
    dotted_path = ".".join(curr.relative_to(glide_root.parent).parts)
    if v.verbosity >= 3:
        click.secho(f"dotted_path={dotted_path}", dim=True)

    return asset_path, import_module(f"{dotted_path}.glideconf")


class SpeakableException(click.ClickException):
    def __init__(self, msg):
        super().__init__(msg)
        subprocess.Popen(["say", msg])
