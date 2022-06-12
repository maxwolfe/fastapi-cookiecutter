"""Unit tests for {{ cookiecutter.project_name }}."""
from {{cookiecutter.project_name}} import __version__


def test_version(expected_version: str):
    assert __version__ == expected_version, f"Expecting Version: {expected_version}"
