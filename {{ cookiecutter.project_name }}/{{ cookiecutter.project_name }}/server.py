"""The application server execution for {{cookiecutter.project_name}}."""
from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

from . import __version__
from .routers import health, root

# Tags Metadata
tags_metadata = [{"name": "root", "description": "General Webserver Operations."}]

# Application Metadata
app = FastAPI(
    title="{{cookiecutter.application_name}}",
    description="""
    {{cookiecutter.project_description}}
    """,
    version=__version__,
)

# Application Routes
app.include_router(root.router)

# Health Route
app.add_api_route("/health", health.router)

# Versioned API
app = VersionedFastAPI(
    app,
    version_format="{major}",
    prefix_format="/v{major}",
)
