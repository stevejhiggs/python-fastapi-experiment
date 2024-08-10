# python-fastapi-experiment

Just me learning the fundamentals of production apis in python. I've not really used python outside of toy examples before so this is my attempt to find "good" patterns in using python.

I'm sure it will be full of non-python ways of doing things and should not be taken as an example to follow.

## Setup

### Via devcontainers

- have the dev containers 

### Directly on your machine

- install [pyenv](https://github.com/pyenv/pyenv) to allow us to dynamically switch python versions per project
- install [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to allow us to scope packages installation to our projects
- run `pyenv virtualenv 3.12.5 python-fastapi-experiment`

This means we now have an isolated version of python ready for our packages

- run `pip install -r requirements.txt` to install dependacies

In order for the items endpoint to function you will need a 

### Setup gotchas

By default vscode will not use the virtualenv you have set up and you'll need to click the "python" option in the bottom bar and select it. The most obvious way this will show up is that vscode will claim it cant find the packages you have installed.

## Questions I still have

- Is there really no way to define a virtualenv in a way that makes setup at least semi-automatic without using a shell script?

- Is there no equivilent of dev only dependancies for things like testing frameworks?