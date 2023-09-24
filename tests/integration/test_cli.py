from unittest.mock import patch

from package_name import cli


@patch("package_name.cli.requests")
@patch("package_name.cli.argparse._sys.argv")
def test_cli_default_command(mock_argv, mock_requests) -> None:
    mock_argv.__getitem__.return_value = []

    cli.run()

    mock_requests.get.assert_not_called()


@patch("package_name.cli.requests")
@patch("package_name.cli.argparse._sys.argv")
def test_cli_zen_command(mock_argv, mock_requests) -> None:
    mock_argv.__getitem__.return_value = ["--zen"]

    cli.run()

    mock_requests.get.assert_called_once_with(url="https://api.github.com/zen", timeout=30)
