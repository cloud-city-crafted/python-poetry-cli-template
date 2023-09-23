import argparse


def run() -> None:
    """Configures arg parser for package-name

    Configures the usage, args and sub-commands for the package-name.
    """
    parser = argparse.ArgumentParser(
        prog="package-name",
        description="Package description",
    )
    parser.print_help()
