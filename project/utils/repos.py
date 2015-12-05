import os
from . import config, constants


def clone_public_data():
    exit_code = os.system("git clone -b master --single-branch {} {}"
        .format(config.get('public_repo'),
        constants.PUBLIC_DATA_DIR))
    return exit_code


def clone_private_data():
    exit_code = os.system("git clone -b master --single-branch {} {}"
        .format(config.get('private_repo'), constants.PRIVATE_DATA_DIR))
    return exit_code
