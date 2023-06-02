from pathlib import Path
import pytest


def _get_repo_root_dir() -> str:
    """
    :return: path to the project folder.
    `tests/` should be in the same folder and this file should be in the root of `tests/`.
    """
    return str(Path(__file__).parent.parent)


ROOT_DIR = _get_repo_root_dir()
RESOURCES = Path(f"{ROOT_DIR}/tests/resources")

@pytest.fixture(
    scope="function",
    params=[
        "LiveData.html",
    ],
)
def ambientweather_data(request) -> str:
    with (RESOURCES / request.param).open("r", encoding="utf8") as data:
        return data.read()
