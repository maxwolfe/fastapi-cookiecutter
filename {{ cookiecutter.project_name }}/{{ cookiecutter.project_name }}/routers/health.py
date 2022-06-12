"""Health Route."""
from fastapi_health import health


def application_health() -> dict[str, str]:
    """The health of my application."""
    return {"application": "healthy"}

router = health([application_health])
