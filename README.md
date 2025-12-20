# 📈 Tech Stocks Risk & Return Analysis (2024-2025)

## 📌 Project Overview
This project performs a quantitative analysis of 5 major tech stocks (**AAPL, MSFT, GOOGL, AMZN, NVDA**) to evaluate their risk-adjusted performance over the last full year.

Using Python, I automated the process of data extraction, statistical calculation (Volatility & Sharpe Ratio), and visualization to identify the most efficient investment opportunities.

## 📊 Methodology
* **Data Source:** Real-time historical data fetched via `yfinance` API (Dates: Jan 2024 - Jan 2025).
* **Metric 1 - Normalization:** Rebased all stock prices to 100 to allow for direct visual comparison of growth.
* **Metric 2 - Risk Analysis:** Calculated annualized volatility (Standard Deviation * sqrt(252)).
* **Metric 3 - Sharpe Ratio:** Evaluated risk-adjusted returns (assuming a risk-free rate of 4%).

## 🛠️ Technologies Used
* **Python 3.x**
* **Pandas & NumPy** (Data Manipulation)
* **Matplotlib** (Data Visualization)
* **Yfinance** (Market Data API)

## 📉 Key Results
The analysis highlights the trade-off between risk and return in the tech sector.
*(See the chart below for visual performance)*

![Stock Analysis Result](results_chart.png)

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
