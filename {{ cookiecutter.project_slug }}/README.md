# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Setup project

    $ uv sync

## Start example app

    $ uv run {{ cookiecutter.project_slug }} --name You

## Run linter, formatter and tests

    $ uv run ruff check
    $ uv run ruff format --check
    $ uv run pytest -s

## Teardown project

    $ rm -r .venv uv.lock
