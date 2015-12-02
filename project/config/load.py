import os
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_CONFIG_DIR = "~/.dfa.yml"

def get_config_data(filename):
    try:
        config_file = open(filename)
        return load(config_file, Loader=Loader)
    except FileNotFoundError:
        return None


DEFAULT_CONFIG = get_config_data(os.path.join(BASE_DIR, 'defaults.yml'))

USER_CONFIG = get_config_data(os.path.expanduser(USER_CONFIG_DIR))

def get_config(key):
    if key in USER_CONFIG:
        return USER_CONFIG[key]
    elif key in DEFAULT_CONFIG:
        return DEFAULT_CONFIG[key]
    return None
