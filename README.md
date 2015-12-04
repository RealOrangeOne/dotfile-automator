# DotFile Automator
Command-Line tool for syncing dotfile-like files and configs between computers, using the power of Git.

## Installation
### Prerequisites
* Python 3
* Pip

__Note__: If you would like the tool to run faster, install `libyml` through your preffered package manager. This will allow reading from the config file faster.
### The Installation Process
Installation can be done using the `install.sh` script in the root of the repo. Simply run it, with or without the repo pre-cloned. This will run through the installation automatically.

## Configuration
Configuration is done using a simple config file in your home directory (`~/.dfa.yml`). This file is used to override the default values for your repo, in case it differs from what is used by default. If this file is not present, the tool can still be used fully.

## Getting Started
After installation, you can test the tool is installed correctly by running:

    dfa --help

If help text is displayed, you're good to go! If not, try repeating the installation steps again, or posting an issue on the issues page.
