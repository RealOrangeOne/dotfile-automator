import click
from project.utils import config

@click.command('export')
@click.argument('sections', nargs=-1)
def cli(sections):
    pass
