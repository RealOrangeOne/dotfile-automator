import os, shutil
from yaml import load
from project.utils import shell, constants

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def atom():
    out, error = shell.call('which apm')
    if not out or error:
        print("You don't seem to have atom installed.")
        return True
    os.chdir('atom')
    packages_themes = []
    with open('packages.yml') as pt_file:
        packages_themes = load(pt_file, Loader=Loader) or {}
    for package in packages_themes:
        exit_code = os.system('apm install {}'.format(package))
        if exit_code != 0:
            print("Error installing {}".format(package), exit_code)
            return True

    shutil.copy2(
        os.path.join(constants.PUBLIC_DATA_DIR, 'atom', 'keymap.cson'),
        os.path.expanduser("~/.atom/keymap.cson")
    )
