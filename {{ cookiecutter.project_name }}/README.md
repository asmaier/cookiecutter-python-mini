# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Setup project

    $ uv sync

## Start example app

    $ uv run python src/{{ cookiecutter.project_slug }}/main.py

## Run linter and tests

    $ uv run ruff check
    $ uv run pytest -s

## Teardown project

    $ rm -r .venv uv.lock