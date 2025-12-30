# Project 03: Algorithmic Trading – Momentum Trend Following (SPY)

## Objective
This project implements a momentum-based algorithmic trading strategy using moving average crossovers on SPY.

## Strategy Logic
- 50-day Simple Moving Average (MA50)
- 200-day Simple Moving Average (MA200)
- Golden Cross → Buy
- Death Cross → Sell
- Signals are shifted to avoid look-ahead bias

## Data
- Asset: SPY (S&P 500 ETF)
- Period: 2020–2024
- Source: Yahoo Finance

## Tools
Python, Pandas, NumPy, Matplotlib, YFinance

## Output
- Strategy performance chart
- Buy/Sell signal visualization
