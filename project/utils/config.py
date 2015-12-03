import os
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_CONFIG_DIR = "~/.dfa.yml"


def get_config_data(filename):
    try:
        config_file = open(filename)
        return load(config_file, Loader=Loader)
    except FileNotFoundError:
        return []


DEFAULT_CONFIG = get_config_data(os.path.join(BASE_DIR, 'defaults.yml'))

USER_CONFIG = get_config_data(os.path.expanduser(USER_CONFIG_DIR))


def get(key):
    if USER_CONFIG and key in USER_CONFIG:
        return USER_CONFIG[key]
    elif DEFAULT_CONFIG and key in DEFAULT_CONFIG:
        return DEFAULT_CONFIG[key]
    return None