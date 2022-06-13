"""Root Schemas."""
from pydantic import BaseModel


class ApplicationHome(BaseModel):
    """Application Root Domain."""

    application_name: str
    version: str
