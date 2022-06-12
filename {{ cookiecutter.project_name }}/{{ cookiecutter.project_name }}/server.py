"""The application server execution for {{cookiecutter.project_name}}."""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from {{cookiecutter.project_name}} import __version__

from .errors import ExposableError
from .routers import health, root
from .schemas import ErrorSchema

# Tags Metadata
tags_metadata = [{"name": "root", "description": "General Webserver Operations."}]

# Application Metadata
app = FastAPI(
    title="{{cookiecutter.application_name}}",
    description="""
    {{cookiecutter.project_description}}
    """,
    version=__version__,
    responses={
        512: {
            "description": "An error that can be exposed to the client.",
            "model": ErrorSchema,
        },
    },
)

# Application Routes
app.include_router(root.router)

# Health Route
app.add_api_route("/health", health.router)


@app.exception_handler(ExposableError)
def exception_handler(request: Request, exc: ExposableError):
    """Handle Exposable Errors."""
    return JSONResponse(
        status_code=512,
        content={
            "message": str(exc),
        },
    )
