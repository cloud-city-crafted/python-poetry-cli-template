import argparse
from importlib import metadata
import requests


def run() -> None:
    """Entrypoint for package-name CLI tool

    Extracts CLI args and orchestrates execution path to run based on the args provided.
    """

    parser = _get_parser()
    args = parser.parse_args()

    if args.version:
        _print_version()
    elif args.zen:
        _print_zen()
    else:
        parser.print_help()


def _print_zen() -> str:
    print(requests.get(url="https://api.github.com/zen", timeout=30).text)


def _get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="package-name", description="Package description")
    parser.add_argument("--version", "-v", action="store_true", help="print version")
    parser.add_argument("--zen", "-z", action="store_true", help="print a random sentence of Zen")

    return parser


def _print_version() -> str:
    print(metadata.version("package-name"))
