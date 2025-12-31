# Project 06 — Applied Option Pricing on Real Market Data

## Overview
This project applies the Black–Scholes option pricing model to real market data.
It retrieves live stock prices, estimates market volatility, and computes theoretical
option prices for practical financial analysis.

## Visualization
The following heatmap illustrates how **Call option prices vary** with changes in
the underlying stock price and market volatility.  
The chart is generated automatically each time the code is executed.

![Applied Option Pricing Heatmap](applied_option_price_heatmap.png)

## Objectives
- Fetch real stock prices automatically
- Estimate annualized volatility from historical returns
- Apply the Black–Scholes pricing model
- Visualize price sensitivity using real market parameters

## Methodology
1. Retrieve historical stock prices using Yahoo Finance
2. Compute log returns and annualized volatility
3. Apply the Black–Scholes closed-form solution
4. Generate a sensitivity heatmap

## Tools & Libraries
- Python
- NumPy
- Pandas
- SciPy
- Matplotlib
- Seaborn
- yFinance

## Notes
- Prices update on each execution
- Market prices may differ from theoretical values due to liquidity and demand

## Author
**Fares Awwad-Zeidan**
