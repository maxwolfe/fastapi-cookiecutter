"""Unit test fixtures."""
from functools import reduce

from fastapi.testclient import TestClient
from pytest import fixture
from {{cookiecutter.project_name}} import server
from {{cookiecutter.project_name}}.dependencies import get_settings
from {{cookiecutter.project_name}}.settings import Settings


@fixture(scope="session")
def expected_version() -> str:
    """The expected software version."""
    return "0.1.0"


@fixture(scope="session")
def application_name() -> str:
    """The Application Name."""
    return "{{cookiecutter.application_name}}"


@fixture(scope="session")
def good_test_settings() -> Settings:
    """Good Test Settings."""
    return Settings(connectivity_url="https://www.httpbin.org/status/200")


@fixture(scope="session")
def bad_test_settings() -> Settings:
    """Bad Test Settings."""
    return Settings(connectivity_url="https://www.httpbin.org/status/400")


@fixture(scope="session")
def test_client(good_test_settings: Settings) -> TestClient:
    """The Web Application's Test Client."""
    client = TestClient(server.app)

    server.app.dependency_overrides[get_settings] = lambda: good_test_settings

    return client


@fixture(scope="session")
def expected_application_health() -> dict[str, str]:
    """Expected application health."""
    return {"application": "healthy"}


@fixture(scope="session")
def healthy_internet_connectivity() -> dict[str, str]:
    """Healthy Internet Connectivity."""
    return {"connectivity": "healthy"}


@fixture(scope="session")
def unhealthy_internet_connectivity() -> dict[str, str]:
    """Unhealthy Internet Connectivity."""
    return {"connectivity": "unhealthy"}


@fixture(scope="session")
def expected_health(
    expected_application_health: dict[str, str],
    healthy_internet_connectivity: dict[str, str],
) -> dict[str, str]:
    """Expected /health response."""
    health_checks = [expected_application_health, healthy_internet_connectivity]

    def merge_dictionaries(health_checks: list[dict[str, str]]) -> dict[str, str]:
        """Merge a list of dictionaries."""
        return reduce(
            lambda first_dict, second_dict: first_dict | second_dict,
            health_checks,
        )

    return merge_dictionaries(health_checks)
