![Applied Option Pricing Heatmap](applied_option_price_heatmap.png)

# Project 06 — Applied Option Pricing on Real Market Data

## Overview
This project applies the **Black–Scholes option pricing model** to **real market data**.
It retrieves live stock prices, estimates market volatility from historical returns,
and computes theoretical Call and Put option prices.

---

## Objectives
- Fetch real stock prices automatically
- Estimate annualized volatility from historical data
- Price Call and Put options using Black–Scholes
- Visualize option price sensitivity using real market parameters

---

## Methodology
1. Retrieve historical stock prices using Yahoo Finance
2. Compute log returns and annualized volatility
3. Apply the Black–Scholes closed-form formula
4. Generate a sensitivity heatmap based on real data

---

## Key Insight
Option prices increase as volatility and underlying stock price increase.
The visualization highlights how uncertainty directly affects option valuation.

---

## Tools & Libraries
- Python
- NumPy
- Pandas
- SciPy
- Matplotlib
- Seaborn
- yFinance

---

## Notes
- The heatmap is generated automatically by the code
- Prices update each time the script is executed
- Market prices may differ from theoretical values due to liquidity and demand

---

## Author
**Fares Awwad-Zeidan**
