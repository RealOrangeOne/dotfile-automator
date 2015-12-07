import click
from project.export import exports
from project.utils import repos


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
    errors = []
    for func in functions:
        try:
            repos.go_to_data()  # Reset data directory
            func()
        except Exception as e:
            errors.append(e)

    if errors:
        print("Errors:")
        for error in errors:
            print(error)
    return 0


def is_function(item):
    return type(item).__name__ == 'function'
