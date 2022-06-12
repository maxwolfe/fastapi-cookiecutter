"""API Dependencies for configuration settings."""
from functools import lru_cache

from ..settings import Settings


@lru_cache
def get_settings() -> Settings:
    """Configuration Settings."""
    return Settings()
