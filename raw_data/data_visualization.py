import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define the directory and file path
cleaned_data_dir = "cleaned_data"
cleaned_file_path = os.path.join(cleaned_data_dir, "nifty_cleaned_data.csv")
visualizations_directory = "Visualizations"
os.makedirs(visualizations_directory, exist_ok = True)

# Check if the cleaned data file exists
if not os.path.exists(cleaned_file_path):
    print("Cleaned data file not found. Please run data_processing.py first.")
    exit()

# Read the cleaned data
df = pd.read_csv(cleaned_file_path)

# Convert 'Date' column to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# --- Create Visualizations ---

# 1. Overall Daily Close Price Trend
plt.figure(figsize=(15, 7))
sns.lineplot(data=df, x='Date', y='Close', hue='ticker')
plt.title('Daily Closing Price Trend for All Tickers')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()
plt.savefig(os.path.join(visualizations_directory, 'daily_closing_price_trend.png'))
plt.close()

# 2. Daily Volume Traded over Time
plt.figure(figsize=(15, 7))
sns.lineplot(data=df, x='Date', y='Volume', hue='ticker')
plt.title('Daily Volume Trend for All Tickers')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()
plt.savefig(os.path.join(visualizations_directory, 'daily_volume_trend.png'))
plt.close()

# 3. Distribution of Daily Returns
plt.figure(figsize=(10, 6))
sns.histplot(df['Daily_Return_Pct'], bins=50, kde=True)
plt.title('Distribution of Daily Returns')
plt.xlabel('Daily Return Percentage')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig(os.path.join(visualizations_directory, 'daily_returns_distribution.png'))
plt.close()

# 4. Average Daily Returns by Ticker
avg_returns = df.groupby('ticker')['Daily_Return_Pct'].mean().sort_values(ascending=False)
plt.figure(figsize=(15, 8))
avg_returns.plot(kind='bar')
plt.title('Average Daily Returns by Ticker')
plt.xlabel('Ticker')
plt.ylabel('Average Daily Return Percentage')
plt.tight_layout()
plt.savefig(os.path.join(visualizations_directory, 'top_20_avg_returns.png'))
plt.close()

print("Visualizations created and saved to the 'Visualizations' folder.")