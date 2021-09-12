#
# https://click.palletsprojects.com/en/8.0.x/complex/
#
# How to play with click. make a git CLI clone

import os
import click


# create a class that we will use as out 'state' for all the things
class Repo(object):
    def __init__(self, home=None, debug=False):
        self.home = os.path.abspath(home or '.')
        self.debug = debug


# create a group command that can have subcommands
@click.group()
@click.option('--repo-home', envvar='REPO_HOME', default='.repo')
@click.option('--debug/--no-debug', default=False, envvar='REPO_DEBUG') 
@click.pass_context
def cli(ctx, repo_home, debug):
    ''' create the click object w/ the state class.
        use decorated so we pass this context and share namespace '''
    ctx.obj = Repo(repo_home, debug)


# define the first child command named clone. 
@cli.command()
@click.argument('src')
@click.argument('dest', required=False)
def clone(src, dest):
    pass


@cli.command()
@click.argument('src')
@click.argument('dest', required=False)
@click.pass_obj
def clone(repo, src, dest):
    """ this one will pass the object instead of using shared mem"""
    pass


# pass_repo = click.make_pass_decorator(Repo)
pass_repo = click.make_pass_decorator(Repo, ensure=True)


@cli.command()
@click.argument('src')
@click.argument('dest', required=False)
@pass_repo
def clone(repo, src, dest):
    pass


@click.command()
@pass_repo
def cp(repo):
    click.echo(isinstance(repo, Repo))
