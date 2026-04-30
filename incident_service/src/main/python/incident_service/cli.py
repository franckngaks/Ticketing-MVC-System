"""Console script for ticket_service."""

import typer
from rich.console import Console

from incident_service import utils

app = typer.Typer()
console = Console()


@app.command()
def main() -> None:
    """Console script for ticket_service."""
    console.print("Replace this message by putting your code into ticket_service.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
