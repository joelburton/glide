import shutil
import subprocess
from pathlib import Path
import time
from dataclasses import dataclass, field

import click
from click_repl import register_repl

from glide import version
from .utils import get_nearest_glideconf, get_glide_root, SpeakableException
from . import verbosity as v

# Convenience API
echo = click.secho

glide_root = get_glide_root()
if not glide_root:
    raise SpeakableException("Glide root not found")
asset_path, glideconf_mod = get_nearest_glideconf(glide_root)

# Used throughout: the Glide instance found in the glideconf
g = glideconf_mod.Glide(asset_path)


@dataclass()
class State:
    """Can be passed between click commands."""

    g = None
    sphinx_opts: dict = field(default_factory=dict)


pass_state = click.make_pass_decorator(State, ensure=True)

gpl = """
Glide copyright (C) 2024 Joel Burton.
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions. You're looking good today.
"""


@click.group(
    epilog=gpl,
    context_settings={
        'help_option_names': ['-h', '--help'],
        'auto_envvar_prefix': 'GLIDE'
    })
@click.version_option(
    str(version),
    "-V", "--version",
    prog_name="Glide")
@click.option(
    '-v', '--verbose',
    count=True,
    help="Repeat to increase verbosity.")
@click.option(
    "-O", "--opt",
    multiple=True,
    help="Sphinx options " + click.style("eg html_theme=handouts", dim=True) + ".")
@click.option(
    "-c", "--cohort",
    required=True)
@click.option(
    "--skip-reqs/--no-skip-reqs",
    help="Skip dependency checking."
)
@click.option('--token', help='Token for SIS.')
@pass_state
def cli(state, verbose, opt, cohort, token, skip_reqs):
    # Set this on the module, so everywhere can import it w/o needing to pass
    v.verbosity = verbose
    g.cohort = cohort
    g.skip_reqs = skip_reqs  # fixme
    state.g = g
    if token:
        g.token = token
    state.sphinx_opts = dict([o.split("=", 2) for o in opt])
    if v.verbosity >= 2:
        echo(f"State: {state}", dim=True)


@cli.command("all")
@click.option('--open/--no-open', "-o", show_default=True, help='Open1')
@pass_state
def all_all(state, open):
    """Build everything."""
    out = g.all_all(state.sphinx_opts)
    if open:
        click.launch(out)


# #########################################################################################

@cli.group(chain=True)
def handouts():
    pass


@handouts.command("make")
@click.option('--open/--no-open', "-o")
@pass_state
def handouts_make(state, open):
    """Build HTML for handouts."""
    out = g.handouts_make(state.sphinx_opts)
    if open:
        click.launch(out)


@handouts.command("publish")
@click.option('--open/--no-open', "-o")
def handouts_publish(open):
    """Publish handouts at SIS."""
    out = g.handouts_publish()
    if open:
        click.launch(out)


@handouts.command("upload")
@click.option('--open/--no-open', "-o")
@click.option('--host', type=click.Choice(['aws', 'netlify']), default='aws')
def handouts_upload(open, host):
    """Upload handouts to S3."""
    out = g.handouts_upload(host)
    if open:
        click.launch(out)


@handouts.command("all")
@click.option('--open/--no-open', "-o")
@pass_state
def handouts_all(state, open):
    """Do everything for handouts."""

    out = g.handouts_all(state.sphinx_opts)
    if open:
        click.launch(out)


# ###########################################################################################

@cli.group(chain=True)
def revealjs():
    pass


@revealjs.command("make")
@click.option('--open/--no-open', "-o")
@pass_state
def revealjs_make(state, open):
    """Build HTML for revealjs."""
    out = g.revealjs_make(state.sphinx_opts)
    if open:
        click.launch(out)


@revealjs.command("publish")
@click.option('--open/--no-open', "-o")
def revealjs_publish(open):
    """Publish revealjs at SIS."""
    out = g.revealjs_publish()
    if open:
        click.launch(out)


@revealjs.command("upload")
@click.option('--open/--no-open', "-o")
def revealjs_upload(open):
    """Upload revealjs to S3."""
    out = g.revealjs_upload()
    if open:
        click.launch(out)


@revealjs.command("all")
@click.option('--open/--no-open', "-o", show_default=True, help='Open1')
@pass_state
def revealjs_all(state, open):
    """Do everything for revealjs."""

    out = g.revealjs_all(state.sphinx_opts)
    if open:
        click.launch(out)


# ###########################################################################################

@cli.group(chain=True)
def prince():
    pass


@prince.command("make")
@click.option('--open/--no-open', "-o")
@pass_state
def prince_make(state, open):
    """Build HTML for prince."""
    out = g.prince_make(state.sphinx_opts)
    if open:
        click.launch(out)


@prince.command("publish")
@click.option('--open/--no-open', "-o")
def prince_publish(open):
    """Publish prince at SIS."""
    out = g.prince_publish()
    if open:
        click.launch(out)


@prince.command("upload")
@click.option('--open/--no-open', "-o")
def prince_upload(open):
    """Upload prince to S3."""
    out = g.prince_upload(presign=open)
    if open:
        click.launch(out)


@prince.command("all")
@click.option('--open/--no-open', "-o", show_default=True, help='Open1')
@pass_state
def prince_all(state, open):
    """Do everything for prince."""

    out = g.prince_all(state.sphinx_opts)
    if open:
        click.launch(out)


# ###########################################################################################


@cli.command()
def make_zip():
    g.make_zip("handouts")


@cli.command()
@click.argument("path", type=Path)
def create(path: Path):
    """Create new asset folder."""

    g.create(path)


@cli.command()
@click.argument("dest", type=Path)
@click.argument("src", type=Path, default=".")
def copy(src: Path, dest: Path):
    """Copy (and de-symlink)."""

    g.copy(src, dest)


@cli.command()
@click.option(
    "-n", "--dry-run",
    is_flag=True,
    help="Show what would be tied, but do nothing")
def clean(dry_run):
    """Tidy junk from repo."""

    g.clean(dry_run=dry_run, path=Path.cwd())


@cli.group("docs")
def docs():
    pass


@docs.command()
def reference():
    """Show reference docs."""

    click.launch(g.docs_reference)


@docs.command()
def cheatsheet():
    """Show cheatsheet docs."""

    click.launch(g.docs_cheatsheet)


@cli.command()
def install():
    for p in [p for p in Path.cwd().rglob("package.json") if "node_modules" not in p.parts]:
        subprocess.run(f"cd {p.parent} && npm i", shell=True, check=True)

    for p in [p for p in Path.cwd().rglob("requirements.txt") if "venv" not in p.parts]:
        subprocess.run(f"cd {p.parent} && python -m venv venv && venv/bin/python3 -m pip install -r requirements.txt",
                       shell=True, check=True)


# If any CLI options in glideconf, add them
for cmd in glideconf_mod.commands:
    cli.add_command(cmd)

register_repl(cli)

if __name__ == '__main__':
    cli(auto_envvar_prefix='GLIDE')

# @click.option('--password', is_flag=False, prompt=True, prompt_required=False)

# test
# find asset by going up until index.rst
# find glide root by going up until conf.py
# gh issue create --title "glide-test: Some test" --label new --body "foo" --assignee "@me"
# glide bug add "Some test" "Description" (will submit w/empty string if none given)
# could add category via glide subclassing :)
# add a theme-maker config
# add profile setup
# have a simple top-level theme opt
# zoom uploader
# this-week-on-sis
# change "all" to go?


# pyperclip  and --copy-url
# https://github.com/sphinx-contrib/typer


# useful for sphinx:
# https://github.com/sphinx-contrib/icon/tree/main/sphinxcontrib/icon
# https://sphinxcontrib-images.readthedocs.io/en/latest/
# https://sphinxcontrib-youtube.readthedocs.io/en/latest/
# https://github.com/sphinx-contrib/video
# https://github.com/sphinx-contrib/sphinxcontrib-runcmd -- where would we use it?
