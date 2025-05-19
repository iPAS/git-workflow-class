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


def main():
    parser = argparse.ArgumentParser(description="Yahoo Finance CLI Scraper")
    parser.add_argument("ticker", help="Stock ticker symbol (e.g. AAPL, TSLA)")
    parser.add_argument("--current", action="store_true", help="Fetch current stock price")
    
    args = parser.parse_args()

    if args.current:
        get_current_price(args.ticker)    
    

if __name__ == "__main__":
    main()