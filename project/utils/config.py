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
            return load(config_file, Loader=Loader) or {}
    except FileNotFoundError:
        return {}
    except Exception as e:
        print("Error:", e)
        return {}


def write_user_config():
    try:
        with open(constants.USER_CONFIG_DIR, 'w') as config_file:
            dump(USER_CONFIG, config_file, indent=4, default_flow_style=False, Dumper=Dumper)
            return "SUCCESS"
    except Exception as e:
        return e


# Create the config file if it doesnt exist already
os.makedirs(constants.DATA_DIR, mode=0o755, exist_ok=True)
open(constants.USER_CONFIG_DIR, 'a').close()


DEFAULT_CONFIG = get_config_data(constants.DEFAULT_CONFIG_DIR)
USER_CONFIG = get_config_data(constants.USER_CONFIG_DIR)


def get(key):
    if key in USER_CONFIG:
        return USER_CONFIG[key]
    elif key in DEFAULT_CONFIG:
        return DEFAULT_CONFIG[key]
    return None


def set(key, value):
    if key not in DEFAULT_CONFIG:
        return "NO_KEY"
    USER_CONFIG[key] = value
    return write_user_config()


def has_basics():
    for key in constants.REQUIRED_KEYS:
        if not get(key):
            return False
    return True
