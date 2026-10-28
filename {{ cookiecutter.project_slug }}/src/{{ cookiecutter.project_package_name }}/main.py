import argparse
import logging

logger = logging.getLogger(__name__)


def main(name: str = "World") -> None:
    logger.info("Hello, %s!", name)


def cli(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", default="World", help="Name of the person to greet")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.FileHandler("example.log", mode="w"), logging.StreamHandler()],
    )
    main(args.name)


if __name__ == "__main__":
    cli()
