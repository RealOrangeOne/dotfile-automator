import click
from project.export import exports
from project.utils import repos, shell


DEFAULT = 'all'


@click.command('export')
@click.argument('sections', nargs=-1, default=DEFAULT)
def cli(sections):
    functions = [f for k, f in exports.__dict__.items() if is_function(f)]
    if sections != DEFAULT:  # If they don't want to export everything
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
            if func.__name__ in sections:
                sections.remove(func)
        except Exception as e:
            errors.append(e)
    if sections:
        if DEFAULT in sections:
            repos.go_to_data()
            out, error = shell.call("make export")
            if error:
                errors.append(error)
        else:
            for item in sections:
                repos.go_to_data()
                out, error = shell.call("make " + item)
                if error:
                    errors.append(error)
                    break
    if errors:
        print("Errors:")
        for error in errors:
            print(error)
        return 1
    return 0


def is_function(item):
    return type(item).__name__ == 'function'
