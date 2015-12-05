import os.path
import click
import logging


FORMAT = "[%(levelname)s]: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logging.getLogger("requests").setLevel(logging.WARNING)


class DotFileCLI(click.MultiCommand):

    def list_commands(self, ctx):
        return ['config', 'sync', 'export']

    def get_command(self, ctx, name):
        ns = {}
        if name not in self.list_commands(ctx):
            return
        fn = os.path.join(os.path.dirname(__file__), name + '/cli.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']

cli = DotFileCLI(help='This tool\'s subcommands are loaded from a plugin folder dynamically.')

if __name__ == '__main__':
    cli()


@click.command(cls=DotFileCLI)
def cli():
    pass
