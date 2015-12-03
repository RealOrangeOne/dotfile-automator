import click
from project.utils import config


@click.command('config')
@click.argument('key')
def cli(key):
    print(config.get(key))
