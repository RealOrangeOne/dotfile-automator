# DotFile Automator [![Circle CI](https://circleci.com/gh/RealOrangeOne/dotfile-automator.svg?style=svg)](https://circleci.com/gh/RealOrangeOne/dotfile-automator)
Command-Line tool for syncing dotfile-like files and configs between computers, using the power of Git.

## Installation
### Prerequisites
* Python 3
* Pip
* Linux / OSX Operating System

__Note__: If you would like the tool to run faster, install `libyml` through your preffered package manager. This will allow reading from the config file faster.
### The Installation Process
Installation can be done using the `install.sh` script in the root of the repo. Simply run it, with or without the repo pre-cloned. This will run through the installation automatically.

Alternatively, you can install it in 1 simple command. This allows you to install it in the best place for your OS, instead od wherever you run the `install.sh` script. The command below may need to be run as a superuser.

    pip3 install git+https://github.com/RealOrangeOne/dotfile-automator.git

## Configuration
Configuration is done using a simple config file in your home directory (`~/.dfa.yml`). This file is used to override the default values for your repo, in case it differs from what is used by default. If this file is not present, the tool can still be used fully.

## Getting Started
After installation, you can test the tool is installed correctly by running:

    dfa --help

If help text is displayed, you're good to go! If not, try repeating the installation steps again, or posting an issue on the issues page.

## Usage
Using `dfa` is very simple, just follow these simple steps:

`dfa config set public_repo <repo-url>`

Set the repo that contains your public data. Replacing `<repo-url>` with the location of your repo, supports both HTTPS and SSH, as well as any Git host.


`dfa config set private_repo <repo-url>` (optional)

Same as previous, but allows you to add private data from outside your main repo, presumably from a private repo. Useful for things like SSH keys, or sensetive environment variables.


`dfa sync [--private]`

Clones the repo into the local directory. Add the `--private` flag to clone the private repo as well, if configured.


`dfa export [sections ...]`

Where the magic happens! Exports the data using presets for certain data types, or can be extended using a [`Make` file](https://en.wikipedia.org/wiki/Makefile). See wiki for how to extend this, and how the presets work. You can specify `sections` to run, that run only the specific sections from the presets, and then from the make file.
