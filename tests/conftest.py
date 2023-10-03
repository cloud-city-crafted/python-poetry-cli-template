import pytest

from pathlib import Path, PosixPath


@pytest.fixture(scope="module")
def project_root() -> PosixPath:
    return Path.cwd().parent
