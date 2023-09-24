import os


def test_cli_default() -> None:
    output = os.popen("poetry run package-name").read()

    assert output == (
        "usage: package-name [-h] [--zen]\n\n"
        "Package description\n\n"
        "options:\n"
        "  -h, --help  show this help message and exit\n"
        "  --zen, -z   print a random sentence of Zen\n"
    ), "should display default output"


def test_cli_zen_flag() -> None:
    output = os.popen("poetry run package-name --zen").read()

    assert output.endswith(".\n"), "should return zen sentence"
    assert "usage" not in output, "should not print usage"
