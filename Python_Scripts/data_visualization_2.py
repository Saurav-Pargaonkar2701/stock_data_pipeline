import pandas as pd
import plotly.express as px
import os

# Define the directory and file paths
cleaned_data_dir = "cleaned_data"
cleaned_file_path = os.path.join(cleaned_data_dir, "nifty_cleaned_data.csv")
visualizations_dir = "visualizations"
os.makedirs(visualizations_dir, exist_ok=True)

# Check if the cleaned data file exists
if not os.path.exists(cleaned_file_path):
    print("Cleaned data file not found. Please run data_processing.py first.")
    exit()

# Read the cleaned data
df = pd.read_csv(cleaned_file_path)

# Convert 'Date' column to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# --- Create Interactive Visualizations and Save them as HTML Files ---

# 1. Overall Daily Close Price Trend
fig_close_trend = px.line(df, x='Date', y='Close', color='ticker', title='Interactive Daily Closing Price Trend for All Tickers')
fig_close_trend.update_layout(
    legend_title_text='Tickers',
    legend=dict(
        orientation="v",
        yanchor="auto",
        y=1,
        xanchor="auto",
        x=1.02,
        traceorder="normal",
        font=dict(size=10),
        itemsizing="constant",
        groupclick="toggleitem",
        bgcolor="rgba(255, 255, 255, 0.5)",
        bordercolor="rgba(0, 0, 0, 0.1)",
        borderwidth=1,
        title_font_size=12
    )
)
fig_close_trend.write_html(os.path.join(visualizations_dir, 'interactive_closing_price_trend.html'))


# 2. Daily Volume Traded over Time
fig_volume_trend = px.line(df, x='Date', y='Volume', color='ticker',
                           title='Interactive Daily Volume Trend for All Tickers')
fig_volume_trend.update_layout(
    legend_title_text='Tickers',
    legend=dict(
        orientation="v",
        yanchor="auto",
        y=1,
        xanchor="auto",
        x=1.02,
        traceorder="normal",
        font=dict(size=10),
        itemsizing="constant",
        groupclick="toggleitem",
        bgcolor="rgba(255, 255, 255, 0.5)",
        bordercolor="rgba(0, 0, 0, 0.1)",
        borderwidth=1,
        title_font_size=12
    )
)
fig_volume_trend.write_html(os.path.join(visualizations_dir, 'interactive_daily_volume_trend.html'))


# 3. Distribution of Daily Returns
fig_returns_dist = px.histogram(df, x='Daily_Return_Pct', nbins=50,
                                title='Interactive Distribution of Daily Returns')
fig_returns_dist.update_traces(marker_color='#1f77b4')
fig_returns_dist.write_html(os.path.join(visualizations_dir, 'interactive_daily_returns_distribution.html'))


# 4. Top 20 Tickers by Average Daily Returns
avg_returns = df.groupby('ticker')['Daily_Return_Pct'].mean().nlargest(20).reset_index()
fig_top20_returns = px.bar(avg_returns, x='ticker', y='Daily_Return_Pct',
                           title='Top 20 Tickers by Average Daily Returns')
fig_top20_returns.write_html(os.path.join(visualizations_dir, 'interactive_top_20_avg_returns.html'))

print("All interactive visualizations created and saved as HTML files in the 'visualizations' folder.")