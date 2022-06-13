"""Execute server via CLI."""
import uvicorn
from typer import Typer

from . import server

app = Typer()


@app.command()
def run(
    host: str = "127.0.0.1",
    port: int = 9001,
) -> None:
    """Execute the server."""
    uvicorn.run(server.app, host=host, port=port)


def cli() -> None:
    """Execute the CLI."""
    app()


if __name__ == "__main__":
    cli()
