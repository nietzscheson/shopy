import subprocess

import typer

app = typer.Typer()


@app.command()
def format():
    """Format the code using black and isort."""
    subprocess.check_call(["poetry", "run", "black", "shopy"])
    subprocess.check_call(["poetry", "run", "isort", "shopy"])
    subprocess.check_call(["poetry", "run", "pycln", "shopy", "tests", "-a"])
    typer.echo("Formatting completed!")


@app.command()
def lint():
    """Lint the code using flake8 & pylint."""
    subprocess.check_call(["poetry", "run", "flake8", "shopy"])
    subprocess.check_call(["poetry", "run", "pylint", "shopy", "errors-only"])
    typer.echo("Linting completed!")


if __name__ == "__main__":
    app()
