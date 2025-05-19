import typer
from commands import fetch, plot, news


app = typer.Typer()
# TODO: Implement then uncomment me
# app.add_typer(fetch.app, name="fetch")
# app.add_typer(plot.app, name="plot")
# app.add_typer(news.app, name="news")


if __name__ == "__main__":
    app()
