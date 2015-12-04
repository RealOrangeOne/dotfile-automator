import click
from project.utils import config, constants

@click.command('sync')
def cli():
    if not config.has_basics():
        print("You do not have all the basic requirements set.")
        return 1
    
