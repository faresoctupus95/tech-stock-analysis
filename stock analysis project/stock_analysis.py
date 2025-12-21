# ---------------------------------------------------------
# PROJECT: Stock Market Performance & Risk Analysis (2024-2025)
# AUTHOR: Fares Zidan
# ---------------------------------------------------------

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 2. CONFIGURATION (UPDATED DATES)
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA']

# UPDATED: Analyzing the most recent full year trend
start_date = '2024-01-01'
end_date = '2025-01-01' 

# 3. DATA INGESTION
print(f"Downloading data from {start_date} to {end_date}...")
data = yf.download(tickers, start=start_date, end=end_date)['Close']

# 4. DATA PROCESSING (Normalization)
normalized_data = (data / data.iloc[0]) * 100

# 5. QUANTITATIVE ANALYSIS
daily_returns = data.pct_change().dropna()

# Annualized Metrics (252 trading days)
avg_daily_return = daily_returns.mean()
annual_return = avg_daily_return * 252

daily_volatility = daily_returns.std()
annual_volatility = daily_volatility * np.sqrt(252)

# Sharpe Ratio (Risk-Free Rate = 4.0% approx for 2024)
risk_free_rate = 0.04 
sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility

# Create Summary Table
metrics_df = pd.DataFrame({
    'Annual Return': annual_return,
    'Annual Volatility': annual_volatility,
    'Sharpe Ratio': sharpe_ratio
})

# Formatting
metrics_df['Annual Return'] = metrics_df['Annual Return'].map("{:.2%}".format)
metrics_df['Annual Volatility'] = metrics_df['Annual Volatility'].map("{:.2%}".format)
metrics_df['Sharpe Ratio'] = metrics_df['Sharpe Ratio'].map("{:.2f}".format)

# 6. VISUALIZATION
plt.figure(figsize=(14, 7))

for ticker in tickers:
    plt.plot(normalized_data.index, normalized_data[ticker], label=ticker, linewidth=2)

plt.title(f'Tech Sector Performance ({start_date} to {end_date})', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Performance (Start = 100)', fontsize=12)
plt.legend(title='Ticker', loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(100, color='black', linewidth=1, linestyle='-')

# 7. OUTPUT
print("\n--- 2024 QUANTITATIVE METRICS ---")
print(metrics_df)
print("\nDisplaying Plot...")
plt.show()