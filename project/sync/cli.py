import click
from project.utils import config, repos


@click.command('sync')
@click.option('--private/--no-private', default=False)
def cli(private):
    if not config.has_basics():
        print("You do not have all the basic requirements set.")
        return 1
    repos.clone_public_data()
    if private:
        repos.clone_public_data()
