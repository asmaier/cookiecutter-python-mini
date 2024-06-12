import argparse
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    handlers=[
                        logging.FileHandler("example.log", mode="w"),
                        logging.StreamHandler()
                    ])


def main(name: str = "World"):
    logging.info(f"Hello, {name}!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="Name of the person to greet")
    args = parser.parse_args()

    main(args.name) if args.name else main()


