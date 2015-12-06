import os, shutil
from distutils.dir_util import copy_tree
from . import config, constants, shell


def clone_public_data():
    if os.path.isdir(constants.PUBLIC_DATA_DIR):
        print("Updating public...")
        initial = os.getcwd()
        go_to_data()
        out, error = shell.call("git pull")
        os.chdir(initial)
        print(out)
    else:
        print("Downloading public data...")
        out, error = shell.call(
            "git clone -b master --single-branch {} {}".format(
                config.get('public_repo'),
                constants.PUBLIC_DATA_DIR
            )
        )
        print(out)
    copy_tree(
        constants.PUBLIC_DATA_DIR,
        constants.ALL_DATA_DIR
    )


def clone_private_data():
    if os.path.isdir(constants.PRIVATE_DATA_DIR):
        print("Updating private data...")
        initial = os.getcwd()
        os.chdir(constants.PRIVATE_DATA_DIR)
        out, error = shell.call("git pull")
        os.chdir(initial)
        print(out)
        return error
    else:
        print("Downloading private data...")
        out, error = shell.call(
            "git clone -b master --single-branch {} {}".format(
                config.get('private_repo'),
                constants.PRIVATE_DATA_DIR
            )
        )
        print(out)

    copy_tree(
        constants.PRIVATE_DATA_DIR,
        constants.ALL_DATA_DIR
    )


def has_data(data):
    public_path = os.path.join(constants.PUBLIC_DATA_DIR, data)
    private_path = os.path.join(constants.PRIVATE_DATA_DIR, data)
    return os.path.isdir(public_path) or os.path.isdir(private_path)


def go_to_data(subdir=''):
    path = os.path.join(constants.PUBLIC_DATA_DIR, subdir)
    os.chdir(path)
    return path


def clean():
    shutil.rmtree(constants.PUBLIC_DATA_DIR)
    shutil.rmtree(constants.PRIVATE_DATA_DIR)
