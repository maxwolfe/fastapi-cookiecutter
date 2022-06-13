"""The application server execution for {{cookiecutter.project_name}}."""
from sys import stdout
from time import time
from uuid import uuid4

from fastapi import FastAPI, Request
from fastapi_versioning import VersionedFastAPI
from loguru import logger

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

# Logging Configuration
logger.remove()
logger.add(
    stdout, format="{time} - {level} - ({extra[request_id]}) {message} ", level="INFO"
)


# Logging Middleware
@app.middleware("http")
@logger.catch
async def logging_middleware(request: Request, call_next):
    with logger.contextualize(request_id=str(uuid4())):
        logger.info("Request Started")

        start_time = time()
        result = await call_next(request)
        execution_time = time() - start_time

        logger.info(f"Request Completed in {execution_time}")

        return result
