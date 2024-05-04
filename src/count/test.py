import typer

app = typer.Typer()


@app.command()
def count(name: str):
    print(f"Length of {name} is {len(name)}")
