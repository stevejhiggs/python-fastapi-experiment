# python-fastapi-experiment

Just me learning the fundamentals of production apis in python. I've not really used python outside of toy examples before so this is my attempt to find "good" patterns in using python.

I'm sure it will be full of non-python ways of doing things and should not be taken as an example to follow.

## Setup

### Via devcontainers

- have the dev containers 

### Directly on your machine

- install [pdm](https://pdm-project.org/) to act as a package manager
- run `pdm install` this will install the packages and setup a virtual environment.

In order for the items endpoint to function you will need a redis server running on localhost.

## Available commands

- `pdm run dev` - run the api in dev mode
- `pdm run test` - run tests
- `pdm run lint` - lint