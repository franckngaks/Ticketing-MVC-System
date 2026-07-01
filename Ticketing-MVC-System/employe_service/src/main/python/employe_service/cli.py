import typer
from .utils import ma_fonction_utilitaire

app = typer.Typer()

@app.command()
def main():
    """
    Point d'entrée du Service Identity.
    """
    typer.echo("🚀 [IDENTITY SERVICE] Système de gestion des collaborateurs opérationnel.")
    ma_fonction_utilitaire()

if __name__ == "__main__":
    app()
