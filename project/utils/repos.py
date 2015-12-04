import os
from . import config


def has_repo_cloned():
    return os.path.isdir('./data')


def clone_public_data():
    exit_code = 0
    exit_code = os.system("git clone -b master --single-branch {} data"
        .format(config.get('public_repo')))
    return exit_code


def clone_private_data():
    exit_code = 0
    exit_code = os.system("git clone -b master --single-branch {} private_data"
        .format(config.get('private_repo')))
    return exit_code
