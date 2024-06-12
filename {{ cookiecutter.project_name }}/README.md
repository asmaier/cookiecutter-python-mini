# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Setup project

    $ poetry install

## Start example app

    $ poetry run python src/{{ cookiecutter.project_slug }}/main.py

## Run linter and tests

    $ poetry run ruff check
    $ poetry run pytest -s

## Teardown project

    $ poetry env remove --all