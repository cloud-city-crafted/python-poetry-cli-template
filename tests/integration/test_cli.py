from unittest.mock import patch

from package_name import cli


@patch("package_name.cli.requests")
@patch("package_name.cli.argparse._sys.argv")
def test_cli_default(mock_argv, mock_requests, capsys) -> None:
    mock_argv.__getitem__.return_value = []

    cli.run()

    assert capsys.readouterr().out.startswith("usage: package-name"), "should Zen sentence"
    mock_requests.get.assert_not_called()


@patch("package_name.cli.requests")
@patch("package_name.cli.argparse._sys.argv")
def test_cli_zen(mock_argv, mock_requests, capsys) -> None:
    mock_requests.get.return_value.text = "Foo."
    mock_argv.__getitem__.return_value = ["--zen"]

    cli.run()

    assert capsys.readouterr().out == "Foo.\n", "should Zen sentence"
    mock_requests.get.assert_called_once_with(url="https://api.github.com/zen", timeout=30)


@patch("package_name.cli.metadata")
@patch("package_name.cli.requests")
@patch("package_name.cli.argparse._sys.argv")
def test_cli_version(mock_argv, mock_requests, mock_metadata, capsys) -> None:
    mock_argv.__getitem__.return_value = ["--version"]
    mock_metadata.version.return_value = "1.1.0a0"

    cli.run()

    assert capsys.readouterr().out == "1.1.0a0\n", "should print version"
    mock_requests.get.assert_not_called()
