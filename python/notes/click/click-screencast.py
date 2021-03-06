#
#
# https://click.palletsprojects.com/en/8.0.x/quickstart/
#

import click
# from click.decorators import group


# @click.command()
# def hello():
#     click.echo('Hello World!')

@click.group()
def cli():
    pass


@click.command()
def initdb():
    click.echo('Initialized the database')


@click.command()
def dropdb():
    click.echo('Dropped the database')


@click.command()
def greet():
    click.echo("Hello, World!")


cli.add_command(initdb)
cli.add_command(dropdb)

if __name__ == '__main__':
    cli()
