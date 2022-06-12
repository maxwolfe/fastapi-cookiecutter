"""Unit tests for health endpoints."""
from fastapi.testclient import TestClient
from {{cookiecutter.project_name}}.routers.health import (
    application_health,
    internet_connectivity,
)
from {{cookiecutter.project_name}}.settings import Settings


def test_application_health(expected_application_health: dict[str, str]) -> None:
    """Test the application health."""
    assert (
        application_health() == expected_application_health
    ), "Unexpected Application Health"


def test_good_internet_connectivity(
    good_test_settings: Settings,
    healthy_internet_connectivity: dict[str, str],
) -> None:
    """Test the internet connectivity."""
    assert (
        internet_connectivity(good_test_settings) == healthy_internet_connectivity
    ), "Unexpected Bad Internet Connectivity"


def test_bad_internet_connectivity(
    bad_test_settings: Settings,
    unhealthy_internet_connectivity: dict[str, str],
) -> None:
    """Test the internet connectivity."""
    assert (
        internet_connectivity(bad_test_settings) == unhealthy_internet_connectivity
    ), "Unexpected Good Internet Connectivity"


def test_health_endpoint(
    test_client: TestClient, expected_health: dict[str, str],
) -> None:
    """Test the /health endpoint."""
    response = test_client.get("/v1/health")

    assert response.status_code == 200, "Expecting HTTP 200"
    assert response.json() == expected_health, "Unexpected Health Values"
