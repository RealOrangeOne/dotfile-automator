import click
from project.utils import config, repos


@click.command('sync')
@click.option('--private/--no-private', default=False, required=False)
@click.option('--clean/--no-clean', default=False, required=False)
def cli(private, clean):
    if clean:
        print("Cleaning")
        repos.clean()
    if not config.has_basics():
        print("You do not have all the basic requirements set.")
        return 1
    error = repos.clone_public_data()
    if error:
        return 1
    if private:
        if not config.get('private_repo'):
            print("private repo not set")
            return 1
        error = repos.clone_private_data()
    return 1 if error else 0
