import os
from yaml import load, dump
from . import constants

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def get_config_data(filename):
    try:
        with open(filename) as config_file:
            return load(config_file, Loader=Loader)
    except FileNotFoundError:
        return {}
    except Exception as e:
        print("Error:", e)
        return {}


def write_user_config(refresh_after=False):
    try:
        with open(constants.USER_CONFIG_DIR, 'w') as config_file:
            dump(USER_CONFIG, config_file, indent=4, default_flow_style=False, Dumper=Dumper)
            return "SUCCESS"
    except Exception as e:
        return e


DEFAULT_CONFIG = get_config_data(constants.DEFAULT_CONFIG_DIR)
USER_CONFIG = get_config_data(os.path.expanduser(constants.USER_CONFIG_DIR))


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


def has_basics():
    for key in constants.REQUIRED_KEYS:
        if not get(key):
            return False
    return True
