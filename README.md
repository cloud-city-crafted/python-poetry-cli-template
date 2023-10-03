# Python Poetry Project Template

<div align="center">
  <img alt="Python + Poetry" src="./.github/images/python-poetry.png" width="250px"/><br/>
  <p>A Python project template for CLIs using Poetry as the dependency manager.</p>

[Poetry](https://python-poetry.org/) | [Python](https://www.python.org)

</div>

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

## 🎧 Quick Start

Ensure [Python](https://www.python.org/downloads), [Python Poetry](https://python-poetry.org/docs/#installation), and [Poe the Poet](https://poethepoet.natn.io/installation.html) are installed.

Dependency installation is managed via `poetry`. Once cloned, you can install dependencies from the project root:

```shell
poetry install
```

Once dependencies are installed, you can run the package-name:

```shell
poetry run package-name
```

And boom! You're ready to customize a Python project! 🎉

## Configuring Developer Standards

Use `git` to install commit message, pre-commit, and pre-push commit hooks:

```shell
git config --local core.hooksPath .github/hooks/
git config --local commit.template .github/.gitmessage
```

These will ensure commit messages are consistent, code is correctly formatted and linted, and tests before committing or pushing.

Style decisions are based on the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

## 🧑🏽‍💻 Running Project Tasks

[`poe`](https://poethepoet.natn.io/index.html) is used as a task runner and its configuration can be found in the `tool.poe.tasks*` sections of [pyproject.toml](./pyproject.toml).

| Command                | Summary                                               | Bash Equivalent                                                                                                                                                                                                   |
| ---------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `poe test`             | Run application test suites that support coverage     | `PYTHONPATH=src poetry run pytest -vv --import-mode=importlib --cov=src/package_name --cov-fail-under=90 --cov=src/package_name --cov-branch --cov-report term-missing:skip-covered tests/unit tests/integration` |
| `poe test-all`         | Run all tests (without coverage)                      | `PYTHONPATH=src pytest -vv --import-mode=importlib`                                                                                                                                                               |
| `poe test-e2e`         | Run e2e tests only                                    | `PYTHONPATH=src poetry run pytest -vv --import-mode=importlib tests/e2e`                                                                                                                                          |
| `poe test-integration` | Run integration tests only (with coverage)            | `PYTHONPATH=src poetry run pytest -vv --import-mode=importlib --cov=src/package_name --cov-fail-under=90 --cov=src/package_name --cov-branch --cov-report term-missing:skip-covered tests/integration`            |
| `poe test-unit`        | Run unit tests only (without coverage)                | `PYTHONPATH=src poetry run pytest -vv --import-mode=importlib tests/unit`                                                                                                                                         |
| `poe check`            | Run all formatting and linting tools against codebase | `poetry run black --check --line-length 100 . && npx --yes prettier@3.0.3 . --no-config --check && poetry run pylint src tests`                                                                                   |
| `poe format`           | Run all formatting tools against codebase             | `poetry run black --check --line-length 100 . && npx --yes prettier@3.0.3 . --no-config --check`                                                                                                                  |
| `poe format-black`     | Run black against Python source code                  | `poetry run black --check --line-length 100 .`                                                                                                                                                                    |
| `poe format-prettier`  | Run prettier against non-Python code                  | `npx --yes prettier@3.0.3 . --no-config --check`                                                                                                                                                                  |
| `poe lint`             | Run all linting tools against codebase                | `poetry run pylint src tests`                                                                                                                                                                                     |
| `poe lint-pylint`      | Lint Python source code and tests with pylint         | `poetry run pylint src tests`                                                                                                                                                                                     |

## 🧪 Testing Configuration

[`pytest`](https://docs.pytest.org/en/7.4.x/) is used as a test runner and its configuration can be found in the `tool.pytest.ini_options` section of [pyproject.toml](./pyproject.toml). [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/index.html) is used as a coverage reporter.

Running `pytest` with no arguments will:

- Automatically add `src` to the `PYTHONPATH` (pythonpath: `src`)
- Increase verbosity (`-vv`)
- Override pytest's historical default import mode to `importlib` which is recommended for new projects (`--import-mode=importlib`)
- Run all available test items in [`./tests/`](./tests)

Tests are grouped into suites using different path names:

```shell
tests/
├── conftest.py
├── ci/
│   └── ...
├── e2e/
│   └── ...
├── integration/
│   └── ...
└── unit/
    └── ...
```

## 🪪 License

This tool is [MIT licensed](./LICENSE).
