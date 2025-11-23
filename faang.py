#!/usr/bin/env python3

"""
# faang.py
# A terminal-run script that:
# 1. Downloads the latest 5-day hourly FAANG stock data.
# 2. Saves it into the data/ folder using a timestamped filename.
# 3. Plots the Close prices and saves the plot into the plots/ folder.
"""

import os
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Download FAANG stock data (last 5 days, hourly) and save to /data as timestamped CSV.
def download_data():
    
    os.makedirs("data", exist_ok=True)

    tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]
    data = yf.download(
        tickers,
        period="5d",
        interval="1h",
        group_by="ticker"
    )

    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"data/{timestamp}.csv"
    data.to_csv(filename)
    print(f"Saved data to: {filename}")
    return filename

# Load the latest CSV and plot the Close prices.
def plot_data():
    
    os.makedirs("plots", exist_ok=True)

    files = [f for f in os.listdir("data") if f.endswith(".csv")]
    if not files:
        raise FileNotFoundError("No CSV files found in the 'data' folder.")

    latest_file = sorted(files)[-1]
    filepath = os.path.join("data", latest_file)

    data = pd.read_csv(filepath, header=[0, 1])

    date_str = latest_file.split("-")[0]

    plt.figure(figsize=(12, 6))

    tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]
    for ticker in tickers:
        plt.plot(data[(ticker, "Close")], label=ticker)

    plt.title(f"Close Prices for FAANG Stocks on {date_str}")
    plt.xlabel("Hourly Intervals (Last 5 Days)")
    plt.ylabel("Close Price ($)")
    plt.legend()

    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    plot_filename = f"plots/{timestamp}.png"

    plt.savefig(plot_filename, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Plot saved to: {plot_filename}")

# Runs the workflow: Downloads data and immediately plots it
def main():
    download_data()
    plot_data()

# Script entry point
if __name__ == "__main__":
    main()