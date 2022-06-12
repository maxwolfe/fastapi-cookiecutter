"""Unit test fixtures."""
from pytest import fixture


@fixture(scope="session")
def expected_version() -> str:
    """The expected software version."""
    return "0.1.0"
