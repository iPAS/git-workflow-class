import typer
import yfinance as yf
import matplotlib.pyplot as plt


app = typer.Typer()


@app.command("history")
def plot_history(ticker: str, period: str = "6mo", ma: str = "20,50"):
    ma_list = [int(m.strip()) for m in ma.split(",")]
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)

    plt.figure(figsize=(10, 5))
    plt.plot(data["Close"], label="Close")
    for m in ma_list:
        plt.plot(data["Close"].rolling(m).mean(), label=f"MA{m}")
    plt.title(f"{ticker} Price History")
    plt.legend()
    plt.grid()
    plt.show()
