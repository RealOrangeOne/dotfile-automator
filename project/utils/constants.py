import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


USER_CONFIG_DIR = os.path.expanduser("~/.dfa.yml")
DEFAULT_CONFIG_DIR = os.path.join(BASE_DIR, 'defaults.yml')


REQUIRED_KEYS = ['public_data']
