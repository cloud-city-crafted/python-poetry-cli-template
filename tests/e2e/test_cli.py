import os
import re

SEMVAR_PATTERN = (
    r"^(?P<major>0|[1-9]\d*)\."
    r"(?P<minor>0|[1-9]\d*)\."
    r"(?P<patch>0|[1-9]\d*)"
    r"(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
    r"(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
)


def test_cli_default() -> None:
    output = os.popen("poetry run package-name").read()

    assert output == (
        "usage: package-name [-h] [--version] [--zen]\n\n"
        "Package description\n\n"
        "options:\n"
        "  -h, --help     show this help message and exit\n"
        "  --version, -v  print version\n"
        "  --zen, -z      print a random sentence of Zen\n"
    ), "should display default output"


def test_cli_zen_flag() -> None:
    output = os.popen("poetry run package-name --zen").read()

    assert output.endswith(".\n"), "should return zen sentence"
    assert "usage" not in output, "should not print usage"


def test_cli_version_flag() -> None:
    output = os.popen("poetry run package-name --version").read()

    match = re.match(SEMVAR_PATTERN, output.strip())
    assert match is not None, "should print a semvar-compliant version"
