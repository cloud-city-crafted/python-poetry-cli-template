from unittest.mock import patch

from package_name import cli


@patch("package_name.cli.argparse")
def test_run(mock_argparse) -> None:
    cli.run()

    mock_argparse.ArgumentParser.assert_called_once_with(
        prog="package-name", description="Package description"
    )
    mock_argparse.ArgumentParser.return_value.print_help.assert_called_once()
