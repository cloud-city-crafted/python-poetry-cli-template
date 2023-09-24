import os


def test_cli_zen_flag() -> None:
    output = os.popen("poetry run package-name --zen").read()

    assert output.endswith(".\n"), "should return zen sentence"
    assert "usage" not in output, "should not print usage"
