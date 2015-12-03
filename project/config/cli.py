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


@cli.command('set')
@click.argument('key', nargs=1)
@click.argument('value', nargs=-1)
def set(key, value):
    key = " ".join(key)
    status = config.set(key, value)
    if status == "SUCCESS":
        print("Repo set to", repo)
        return 0
    elif status == "NO_KEY":
        print("Key {} not found".format(key))
        return 1
    else:
        print("Something went wrong:", status)
        return 1
