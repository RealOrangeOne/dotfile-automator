import os
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_CONFIG_DIR = os.path.expanduser("~/.dfa.yml")
DEFAULT_CONFIG_DIR = os.path.join(BASE_DIR, 'defaults.yml')


def get_config_data(filename):
    try:
        with open(filename) as config_file:
            return load(config_file, Loader=Loader)
    except FileNotFoundError:
        return {}


def write_user_config(refresh_after=False):
    try:
        with open(USER_CONFIG_DIR, 'w') as config_file:
            dump(USER_CONFIG, config_file, indent=4, default_flow_style=False, Dumper=Dumper)
            return "SUCCESS"
    except Exception as e:
        return e

DEFAULT_CONFIG = get_config_data(DEFAULT_CONFIG_DIR)


USER_CONFIG = get_config_data(os.path.expanduser(USER_CONFIG_DIR))


def get(key):
    if USER_CONFIG and key in USER_CONFIG:
        return USER_CONFIG[key]
    elif DEFAULT_CONFIG and key in DEFAULT_CONFIG:
        return DEFAULT_CONFIG[key]
    return None


def set(key, value, refresh_after=False):
    if key not in DEFAULT_CONFIG:
        return "NO_KEY"
    USER_CONFIG[key] = value
    return write_user_config(refresh_after)
