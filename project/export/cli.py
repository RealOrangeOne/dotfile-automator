import click
from project.export import exports


@click.command('export')
@click.argument('sections', nargs=-1)
def cli(sections):
    functions = [f for k, f in exports.__dict__.items() if is_function(f)]
    if sections:  # If they don't want to export everything
        temp_functions = functions
        functions = []
        for func in temp_functions:
            if func.__name__ in sections:
                functions.append(func)
    for func in functions:
        func()
    return 0


def is_function(item):
    return type(item).__name__ == 'function'
