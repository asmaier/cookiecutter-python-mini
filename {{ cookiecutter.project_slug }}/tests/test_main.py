import logging

from {{ cookiecutter.project_package_name }} import main


def test_main(caplog):
    with caplog.at_level(logging.INFO):
        main.main()
        assert "Hello, World!" in caplog.text

        main.main("Test")
        assert "Hello, Test!" in caplog.text


def test_cli(caplog, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    with caplog.at_level(logging.INFO):
        main.cli(["--name", "CLI"])
        assert "Hello, CLI!" in caplog.text
