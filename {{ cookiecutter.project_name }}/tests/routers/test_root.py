"""Unit tests for root router."""
from fastapi.testclient import TestClient

from {{cookiecutter.project_name}}.routers import root


def test_home(
    expected_version: str,
    application_name: str,
) -> None:
    """Test the home endpoint."""
    application_home = root.home()

    assert (
        application_home.application_name == application_name
    ), f"Expected application name: {application_name}"

    assert (
        application_home.version == expected_version
    ), f"Expected version: {expected_version}"


def test_home_web(
    test_client: TestClient,
    expected_version: str,
    application_name: str,
) -> None:
    """Test the home endpoint from FastAPI Test Client."""
    response = test_client.get("/v1/")

    assert response.status_code == 200, "Expected HTTP 200"
    assert response.json() == {
        "application_name": application_name,
        "version": expected_version,
    }, "Unexpected JSON Response"
