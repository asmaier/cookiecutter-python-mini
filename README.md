# Cookiecutter Python Mini

This is a Cookiecutter template that can be used to initiate a minimal Python project with a minimal set of tools for development
and testing. It supports the following features:

- [uv](https://docs.astral.sh/uv/) for dependency management
- Linting and formatting with [ruff](https://docs.astral.sh/ruff/)
- Testing with [pytest](https://docs.pytest.org/)

## Quickstart

First you need to [install uv](https://docs.astral.sh/uv/getting-started/installation/), e.g.

    $ curl -LsSf https://astral.sh/uv/install.sh | sh

or on Mac OS X with Homebrew

    $ brew install uv

Then navigate to the directory in which you want to create a project directory, and run

    $ uvx cookiecutter gh:asmaier/cookiecutter-python-mini

`uvx` runs cookiecutter without installing it permanently.

Afterwards your project directory is ready. For a project named `My Project` it will have the following structure
```
my-project/
├── .gitignore
├── README.md
├── pyproject.toml
├── src
│   └── my_project
│       ├── resources
│       │   └── .gitkeep
│       ├── __init__.py
│       └── main.py
└── tests
    ├── resources
    │   └── .gitkeep
    └── test_main.py
```
The project directory and distribution name (`my-project`) are derived from the project name with hyphens,
the importable package name (`my_project`) with underscores.

The code for your python package goes into the `src/my_project` directory.
The tests for your code go into the `tests` directory. Your package and test directory
hold a `resources` directory which is meant for static resources like images, test files, ...
which your package or tests might need.

Just change into the newly created directory, install the dependencies and run the example app

    $ cd my-project
    $ uv sync
    $ uv run my-project --name You

You are now ready to start developing.

That's all Folks! For more information also have a look at the `README.md` created for your project.

## Developing this template

The tests in `tests/` generate projects from the template and run ruff, pytest and the example app in them:

    $ uv run pytest

## Acknowledgements

This project is inspired by 

- https://github.com/fpgmaas/cookiecutter-poetry
- https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
- https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html
