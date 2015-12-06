import click
from project.utils import config


@click.group('config')
def cli():
    pass


@cli.command('show')
@click.argument('key', nargs=-1)
def show(key):
    key = " ".join(key)
    if not key:
        for key, value in config.get_all().items():
            print("{}: {}".format(key, value))
        return 0
    print("'{}' is set to '{}'".format(key, config.get(key)))
    return 0


@cli.command('set')
@click.argument('key', nargs=1)
@click.argument('value', nargs=-1)
def set(key, value):
    if isinstance(value, tuple):
        value = " ".join(value)
    status = config.set(key, value)
    if status == "SUCCESS":
        print("{} set to {}".format(key, value))
        return 0
    elif status == "NO_KEY":
        print("Key {} not found".format(key))
        return 1
    else:
        print("Something went wrong:", status)
        return 1
