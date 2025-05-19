import yfinance as yf
import argparse
import sys
import pandas as pd
import matplotlib.pyplot as plt

def get_current_price(ticker):
    stock = yf.Ticker(ticker)
    price = stock.info.get("currentPrice")
    if price is None:
        print(f"[Error] Could not fetch price for {ticker}")
        return
    print(f"{ticker} current price: ${price}")

def download_history(ticker, start, end, output):
    stock = yf.Ticker(ticker)
    df = stock.history(start=start, end=end)
    if df.empty:
        print(f"[Error] No data found for {ticker} between {start} and {end}")
        return
    df.to_csv(output)
    print(f"[Success] Historical data saved to {output}")

def plot_csv(file_path):
    try:
        df = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
    except Exception as e:
        print(f"[Error] Could not read {file_path}: {e}")
        return

    if "Close" not in df.columns:
        print(f"[Error] No 'Close' column in CSV")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["Close"], label="Close Price", linewidth=2)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title("Stock Price Over Time")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Yahoo Finance CLI Scraper")
    parser.add_argument("ticker", nargs="?", help="Stock ticker symbol (e.g. AAPL, TSLA)")
    parser.add_argument("--current", action="store_true", help="Fetch current stock price")
    parser.add_argument("--history", action="store_true", help="Download historical data")
    parser.add_argument("--start", help="Start date for history (YYYY-MM-DD)")
    parser.add_argument("--end", help="End date for history (YYYY-MM-DD)")
    parser.add_argument("--output", help="CSV output file path", default="history.csv")
    parser.add_argument("--plot", help="Plot historical data from CSV file")

    args = parser.parse_args()

    if args.current:
        if not args.ticker:
            print("[Error] Please provide a ticker symbol.")
            sys.exit(1)
        get_current_price(args.ticker)

    if args.history:
        if not args.ticker:
            print("[Error] Please provide a ticker symbol.")
            sys.exit(1)
        if not args.start or not args.end:
            print("[Error] Start and end dates are required for historical data.")
            sys.exit(1)
        download_history(args.ticker, args.start, args.end, args.output)

    if args.plot:
        plot_csv(args.plot)

if __name__ == "__main__":
    main()
