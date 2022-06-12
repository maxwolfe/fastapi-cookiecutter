"""The root domain for {{cookiecutter.project_name}}."""
from fastapi import APIRouter
from {{cookiecutter.project_name}} import __version__

from ..schemas import ApplicationHome

router = APIRouter(
    prefix="",
    tags=["root"],
)


@router.get(
    "/",
    response_model=ApplicationHome,
)
def home() -> ApplicationHome:
    return ApplicationHome(
        application_name="{{cookiecutter.project_name}}",
        version=__version__,
    )
