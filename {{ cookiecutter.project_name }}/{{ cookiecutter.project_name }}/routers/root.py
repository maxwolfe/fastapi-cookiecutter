"""The root domain for {{cookiecutter.project_name}}."""
from fastapi import APIRouter
from fastapi_versioning import version

from .. import __version__
from ..schemas import ApplicationHome

router = APIRouter(
    prefix="",
    tags=["root"],
)


@router.get(
    "/",
    response_model=ApplicationHome,
)
@version(1)
def home() -> ApplicationHome:
    return ApplicationHome(
        application_name="{{cookiecutter.application_name}}",
        version=__version__,
    )
