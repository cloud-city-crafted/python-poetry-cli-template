from unittest.mock import patch

from package_name import cli


@patch("package_name.cli.argparse")
@patch("package_name.cli.requests")
def test_run_with_no_args(mock_requests, mock_argparse) -> None:
    mock_argparse.ArgumentParser.return_value.parse_args.return_value.zen = False

    cli.run()

    mock_argparse.ArgumentParser.assert_called_once_with(
        prog="package-name", description="Package description"
    )
    mock_requests.get.assert_not_called()
    mock_argparse.ArgumentParser.return_value.print_help.assert_called_once()


@patch("package_name.cli.argparse")
@patch("package_name.cli.requests")
def test_run_with_zen_flag(mock_requests, mock_argparse) -> None:
    mock_argparse.ArgumentParser.return_value.parse_args.return_value.zen = True

    cli.run()

    mock_requests.get.assert_called_once_with(url="https://api.github.com/zen", timeout=30)
    mock_argparse.ArgumentParser.return_value.print_help.assert_not_called()
