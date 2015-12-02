import click
from project.utils import get_config

@click.command('config')
@click.argument('key')
def cli(key):
    print(get_config(key))
    pass
