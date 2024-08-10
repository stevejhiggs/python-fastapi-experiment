# python-fastapi-experiment

Just me learning the fundamentals of production apis in python. I've not really used python outside of toy examples before so this is my attempt to find "good" patterns in using python.

I'm sure it will be full of non-python ways of doing things and should not be taken as an example to follow.

## Setup

### Via devcontainers

- have the dev containers 

### Directly on your machine

- install [poetry](https://python-poetry.org/) to act as a package manager
- run `poetry install` this will install the packages and setup a virtual environment.

In order for the items endpoint to function you will need a redis server running on localhost.

### Setup gotchas

By default vscode will not use the virtualenv you have set up and you'll need to use the Python: Select Interpreter command from the Command Palette (⇧⌘P) and select the `Poetry` venv.

The most obvious way this will show up is that vscode will claim it cant find the packages you have installed.

## Available commands

- `poetry run fastapi dev src/main.py` - run the api in dev mode
- `poetry run pytest` - run tests
- `poetry run ruff check` - lint