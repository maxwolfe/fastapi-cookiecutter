"""Error Schemas."""
from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """An error schema."""

    message: str
