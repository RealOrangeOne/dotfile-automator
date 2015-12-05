import os

# Core Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.expanduser("~/dfa/")

# Config
USER_CONFIG_DIR = os.path.join(DATA_DIR, ".dfa.yml")
DEFAULT_CONFIG_DIR = os.path.join(BASE_DIR, 'defaults.yml')
REQUIRED_KEYS = ['public_data']

# Data Directories
PRIVATE_DATA_DIR = os.path.join(DATA_DIR, 'private_data')
PUBLIC_DATA_DIR = os.path.join(DATA_DIR, 'public_data')
