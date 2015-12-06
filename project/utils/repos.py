import os, shutil
from distutils.dir_util import copy_tree
from . import config, constants, shell


def clone_public_data():
    if os.path.isdir(constants.PUBLIC_DATA_DIR):
        initial = os.getcwd()
        go_to_data()
        out, error = shell.call("git pull")
        os.chdir(initial)
        if error:
            print("Error:", out)
        return error

    out, error = shell.call(
        "git clone -b master --single-branch {} {}".format(
        config.get('public_repo'),
        constants.PUBLIC_DATA_DIR)
    )
    return error


def clone_private_data():
    exit_code = 0
    if os.path.isdir(constants.PRIVATE_DATA_DIR):
        initial = os.getcwd()
        os.chdir(constants.PRIVATE_DATA_DIR)
        out, error = shell.call("git pull")
        os.chdir(initial)
        if error:
            print("Error:", out)
        return error
    else:
        out, error = shell.call(
        "git clone -b master --single-branch {} {}".format(
            config.get('private_repo'),
            constants.PRIVATE_DATA_DIR)
        )
    if error:
        return error

    copy_tree(
        constants.PRIVATE_DATA_DIR,
        constants.PUBLIC_DATA_DIR
    )
    return error


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
