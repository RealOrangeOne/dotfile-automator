import os, shutil
from . import config, constants


def clone_public_data():
    exit_code = os.system("git clone -b master --single-branch {} {}"
        .format(config.get('public_repo'),
        constants.PUBLIC_DATA_DIR))
    return exit_code


def clone_private_data():
    exit_code = os.system("git clone -b master --single-branch {} {}"
        .format(config.get('private_repo'), constants.PRIVATE_DATA_DIR))
    if exit_code != 0:
        return exit_code

    shutil.copytree(
        constants.PRIVATE_DATA_DIR,
        constants.PUBLIC_DATA_DIR
    )


def has_data(data):
    public_path = os.path.join(constants.PUBLIC_DATA_DIR, data)
    private_path = os.path.join(constants.PRIVATE_DATA_DIR, data)
    return os.path.isdir(public_path) or os.path.isdir(private_path)


def go_to_data(subdir=''):
    path = os.path.join(constants.PUBLIC_DATA_DIR, subdir)
    os.chdir(path)
    return path
