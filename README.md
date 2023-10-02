# Python Poetry Project Template

<div align="center">
  <img alt="Python + Poetry" src="./.github/images/python-poetry.png" width="250px"/><br/>
  <p>A Python project template for CLIs using Poetry as the dependency manager.</p>

[Poetry](https://python-poetry.org/) | [Python](https://www.python.org)

</div>

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

## 🎧 Quick Start

Ensure [Python](https://www.python.org/downloads) and [Python Poetry](https://python-poetry.org/docs/#installation) are installed.

Dependency installation is managed via `poetry`. Once cloned, you can install dependencies from the project root:

```shell
poetry install
```

Once dependencies are installed, you can run the package-name:

```shell
poetry run package-name
```

And boom! You're ready to customize a Python project! 🎉

## 🧪 Running Tests

[`pytest`](https://docs.pytest.org/en/7.4.x/) is used as a test runner and its configuration can be found in the `tool.pytest.ini_options` section of [pyproject.toml](./pyproject.toml). [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/index.html) is used as a coverage reporter.

Running `pytest` with no arguments will:

- Automatically add `src` to `PYTHONPATH` (pythonpath: `src`)
- Only run unit tests (testpaths: `tests/unit/package_name`)
- Increase verbosity (`-vv`)
- Calculate coverage (using `pytest-cov`) and display any modules missing coverage

You can specify different paths to run different groupings of tests:

```shell
pytest tests/unit         # Run unit tests
pytest tests/integration  # Run integration tests
pytest tests/e2e          # Run end-to-end tests
pytest tests              # Run all tests
```

### (Optional) Running CI Workflow Tests

Ensure [Docker](https://docs.docker.com/get-docker/) and [`act`](https://github.com/nektos/act#installation) are installed and a [github-act-cache-server](https://github.com/sp-ricard-valverde/github-act-cache-server) is up and running.

Local workflow runs are executed via `act`. Once all dependencies are setup, you can test workflows with:

```shell
# TBD script to run all tests
```

See [example `act` commands](https://github.com/nektos/act#example-commands) to better understand how to run GitHub actions locally.

## Configuring Developer Standards

Use `git` to install commit message, pre-commit, and pre-push commit hooks:

```shell
git config --local core.hooksPath .github/hooks/
git config --local commit.template .github/.gitmessage
```

These will ensure commit messages are consistent, code is correctly formatted and linted, and tests before committing or pushing.

Style decisions are based on the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

## 🪪 License

This tool is [MIT licensed](./LICENSE).
