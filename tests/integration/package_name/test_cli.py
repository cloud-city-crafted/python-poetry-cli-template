import os


def test_default_command() -> None:
    output = os.popen("package-name").read()

    assert output == (
        "usage: package-name [-h]\n\n"
        "Package description\n\n"
        "options:\n"
        "  -h, --help  show this help message and exit\n"
    ), "should display default output"
