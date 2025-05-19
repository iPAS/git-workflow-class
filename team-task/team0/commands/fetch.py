import typer
import yfinance as yf
import pandas as pd


app = typer.Typer()


@app.command("price")
def fetch_price(ticker: str):
    stock = yf.Ticker(ticker)
    price = stock.history(period="1d")["Close"].iloc[-1]
    typer.echo(f"{ticker} latest price: ${price:.2f}")


@app.command("info")
def fetch_info(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info
    typer.echo(pd.Series(info))


@app.command("history")
def fetch_history(ticker: str, period: str = "1mo", interval: str = "1d"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    typer.echo(hist.tail())
