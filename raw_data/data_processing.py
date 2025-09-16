import pandas as pd
import os

# Define directories
raw_data_dir = "raw_data"
cleaned_data_dir = "cleaned_data"
os.makedirs(cleaned_data_dir, exist_ok=True)

# List to hold all dataframes
all_dfs = []

# Get a list of all CSV files in the raw_data directory
for filename in os.listdir(raw_data_dir):
    if filename.endswith('.csv'):
        file_path = os.path.join(raw_data_dir, filename)
        try:
            # Read each CSV file into a pandas DataFrame
            df = pd.read_csv(file_path)
            all_dfs.append(df)
        except Exception as e:
            print(f"Failed to read {filename}. Error: {e}")

# Check if any data was loaded
if not all_dfs:
    print("No data files found to process. Please run data_ingestion.py first.")
    exit()

# Concatenate all dataframes into a single dataframe
consolidated_df = pd.concat(all_dfs, ignore_index=True)

print("Raw data consolidation complete. Shape:", consolidated_df.shape)

# --- Data Cleaning and Transformation ---

# 1. Handle missing values
# Drop rows where the 'Close' price is missing
consolidated_df.dropna(subset=['Close'], inplace=True)

# 2. Convert data types
# The 'Date' column might be a string, so we'll convert it to a datetime object
consolidated_df['Date'] = pd.to_datetime(consolidated_df['Date'])

# Explicitly convert numeric columns to a numeric data type, forcing errors to NaN.
# 'Adj Close' is removed from this list to prevent errors.
numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
for col in numeric_cols:
    if col in consolidated_df.columns:
        consolidated_df[col] = pd.to_numeric(consolidated_df[col], errors='coerce')

# Drop any rows that couldn't be converted to a number
consolidated_df.dropna(subset=numeric_cols, inplace=True)

# 3. Feature Engineering (Adding new columns)
# Calculate daily price change
consolidated_df['Daily_Change'] = consolidated_df['Close'] - consolidated_df['Open']

# Calculate daily return percentage
consolidated_df['Daily_Return_Pct'] = (consolidated_df['Daily_Change'] / consolidated_df['Open']) * 100

# Extract month, day of week, and year for potential analysis
consolidated_df['Year'] = consolidated_df['Date'].dt.year
consolidated_df['Month'] = consolidated_df['Date'].dt.month
consolidated_df['Day_of_Week'] = consolidated_df['Date'].dt.dayofweek

# 4. Filter data
# Remove any rows with zero or negative 'Volume'
consolidated_df = consolidated_df[consolidated_df['Volume'] > 0]

# Reorder columns for better readability. 'Adj Close' has been removed from this list.
final_df = consolidated_df[['ticker', 'Date', 'Year', 'Month', 'Day_of_Week', 'Open', 'High', 'Low', 'Close', 'Volume', 'Daily_Change', 'Daily_Return_Pct']]

print("Data cleaning and transformation complete. Final shape:", final_df.shape)

# --- Save the cleaned data ---

cleaned_file_path = os.path.join(cleaned_data_dir, "nifty_cleaned_data.csv")
final_df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")