import click
from project.utils import config


@click.group('config')
def cli():
    pass


@cli.command('show')
@click.argument('key', nargs=-1)
def show(key):
    key = " ".join(key)
    print(config.get(key))
    return 0
