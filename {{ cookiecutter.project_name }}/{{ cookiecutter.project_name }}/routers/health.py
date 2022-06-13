"""Health checks for the application."""
import requests
from fastapi import Depends
from fastapi_health import health

from ..dependencies import get_settings
from ..settings import Settings


def application_health() -> dict[str, str]:
    """The health of my application."""
    return {"application": "healthy"}


def internet_connectivity(settings: Settings = Depends(get_settings)) -> dict[str, str]:
    """Validate the internet connectivity."""
    response = requests.get(settings.connectivity_url)

    return {"connectivity": "healthy" if response.status_code == 200 else "unhealthy"}


router = health([application_health, internet_connectivity])
