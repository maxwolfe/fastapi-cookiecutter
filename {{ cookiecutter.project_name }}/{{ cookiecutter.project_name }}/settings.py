"""Configuration Settings."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Configuration Settings."""

    connectivity_url: str = "https://www.google.com"
