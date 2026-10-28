import os
import subprocess

import pytest


def run(cmd: list[str], cwd) -> None:
    # Drop the outer venv so `uv run` uses the generated project's own environment
    env = {k: v for k, v in os.environ.items() if k != "VIRTUAL_ENV"}
    subprocess.run(cmd, cwd=cwd, env=env, check=True)


@pytest.mark.parametrize("project_name", ["Python Project", "My-Cool_App"])
def test_bake_and_check(cookies, project_name):
    result = cookies.bake(extra_context={"project_name": project_name})

    assert result.exit_code == 0, result.exception
    project = result.project_path
    package_name = result.context["project_package_name"]
    assert project.name == result.context["project_slug"]
    assert (project / "src" / package_name / "main.py").is_file()
    assert (project / ".gitignore").is_file()

    run(["uv", "run", "ruff", "check"], project)
    run(["uv", "run", "ruff", "format", "--check"], project)
    run(["uv", "run", "pytest", "-q"], project)
    run(["uv", "run", result.context["project_slug"], "--name", "Bake"], project)
