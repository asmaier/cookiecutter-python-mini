import logging

from {{ cookiecutter.project_slug }} import main


def test_main(caplog):
    with caplog.at_level(logging.INFO):
        main.main()
        assert "Hello, World!" in caplog.text

        main.main("Test")
        assert "Hello, Test!" in caplog.text