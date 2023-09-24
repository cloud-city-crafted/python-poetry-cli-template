import subprocess


def test_default_command() -> None:
    with subprocess.Popen(args=["package-name"], stdout=subprocess.PIPE) as proc:
        output = proc.stdout.read()

    assert output.decode() == (
        "usage: package-name [-h] [--zen]\n\n"
        "Package description\n\n"
        "options:\n"
        "  -h, --help  show this help message and exit\n"
        "  --zen, -z   print a random sentence of Zen\n"
    ), "should display default output"
