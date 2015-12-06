import click
from project.utils import config, repos


@click.command('sync')
@click.option('--private/--no-private', default=False)
def cli(private):
    if not config.has_basics():
        print("You do not have all the basic requirements set.")
        return 1
    exit_code = repos.clone_public_data()
    if private and exit_code == 0:
        if not config.get('private_repo'):
            print("private repo not set")
        exit_code = repos.clone_public_data()
    return exit_code
