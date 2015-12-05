import click
from project.export import exports


@click.command('export')
@click.argument('sections', nargs=-1)
def cli(sections):
    functions = [f for k, f in exports.__dict__.items() if is_function(f)]
    print("got all functions", functions)
    if sections:  # If they don't want to export everything
        print("YOu specified sections")
        for func in functions:
            if func.__name__ not in sections:
                print("{} not in {}".format(func.__name__, sections))
                functions.remove(func)
    print("Calling functions", functions)
    for func in functions:
        print("Calling", func.__name__)
        func()
    return 0


def is_function(item):
    return type(item).__name__ == 'function'
