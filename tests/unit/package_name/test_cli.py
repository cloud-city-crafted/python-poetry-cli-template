import argparse

from package_name import cli


def test_get_parser() -> None:
    parser = cli._get_parser()  # pylint: disable=W0212
    args = parser.parse_args(["--zen"])

    assert isinstance(parser, argparse.ArgumentParser), "should instantiate parser instance"
    assert parser.prog == "package-name", "should set CLI tool name"
    assert parser.description == "Package description", "should set CLI tool description"
    assert args.zen, "should parse zen flag to True"
