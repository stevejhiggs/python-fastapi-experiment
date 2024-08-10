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

## Available commands

- `poetry run dev` - run the api in dev mode
- `poetry run pytest` - run tests
- `poetry run ruff check` - lint