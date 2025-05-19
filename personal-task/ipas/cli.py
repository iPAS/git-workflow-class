import yfinance as yf
import argparse
import sys


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


def main():
    parser = argparse.ArgumentParser(description="Yahoo Finance CLI Scraper")
    parser.add_argument("ticker", help="Stock ticker symbol (e.g. AAPL, TSLA)")
    parser.add_argument("--current", action="store_true", help="Fetch current stock price")
    parser.add_argument("--history", action="store_true", help="Download historical data")
    parser.add_argument("--start", help="Start date for history (YYYY-MM-DD)")
    parser.add_argument("--end", help="End date for history (YYYY-MM-DD)")
    parser.add_argument("--output", help="CSV output file path", default="history.csv")
    
    args = parser.parse_args()

    if args.current:
        get_current_price(args.ticker)    

    if args.history:
        if not args.start or not args.end:
            print("[Error] Start and end dates are required for historical data.")
            sys.exit(1)
        download_history(args.ticker, args.start, args.end, args.output)


if __name__ == "__main__":
    main()