import yfinance as yf
import pandas as pd
import os

# Define the directory to save the data
data_dir = "raw_data"
os.makedirs(data_dir, exist_ok=True)

# Hard-coded list of Nifty 200 tickers. This eliminates web scraping errors.
tickers = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS", "INFY.NS",
    "BHARTIARTL.NS", "SBIN.NS", "LICI.NS", "LT.NS", "HCLTECH.NS",
    "ITC.NS", "KOTAKBANK.NS", "AXISBANK.NS", "MARUTI.NS", "ADANIENT.NS",
    "BAJFINANCE.NS", "SUNPHARMA.NS", "HINDUNILVR.NS", "WIPRO.NS", "TITAN.NS",
    "ASIANPAINT.NS", "ULTRACEMCO.NS", "M&M.NS", "ADANIPORTS.NS", "JSWSTEEL.NS",
    "NTPC.NS", "TATASTEEL.NS", "ONGC.NS", "POWERGRID.NS", "NESTLEIND.NS",
    "INDUSINDBK.NS", "COALINDIA.NS", "BAJAJFINSV.NS", "GRASIM.NS", "TECHM.NS",
    "APOLLOHOSP.NS", "DRREDDY.NS", "EICHERMOT.NS", "GAIL.NS", "GRASIM.NS",
    "HCLTECH.NS", "HDFCBANK.NS", "HINDALCO.NS", "HINDUNILVR.NS", "ICICIBANK.NS",
    "INDUSINDBK.NS", "INFY.NS", "IOC.NS", "JINDALSTEL.NS", "JSWSTEEL.NS",
    "KOTAKBANK.NS", "LT.NS", "LTIM.NS", "MARUTI.NS", "M&M.NS", "NESTLEIND.NS",
    "NTPC.NS", "ONGC.NS", "POWERGRID.NS", "RELIANCE.NS", "SBIN.NS",
    "SUNPHARMA.NS", "TATAMOTORS.NS", "TATASTEEL.NS", "TCS.NS", "TITAN.NS",
    "ULTRACEMCO.NS", "UPL.NS", "VEDL.NS", "WIPRO.NS", "ZEEL.NS", "ADANIPORTS.NS",
    "ADANIPOWR.NS", "AMBUJACEM.NS", "ASHOKLEY.NS", "ASIANPAINT.NS", "AUROPHARMA.NS",
    "AXISBANK.NS", "BAJAJ-AUTO.NS", "BAJFINANCE.NS", "BANDHANBNK.NS", "BANKBARODA.NS",
    "BHEL.NS", "BIOCON.NS", "BOSCHLTD.NS", "BRITANNIA.NS", "CADILAHC.NS",
    "CANBK.NS", "CIPLA.NS", "COALINDIA.NS", "DLF.NS", "DABUR.NS",
    "DISHTV.NS", "EICHERMOT.NS", "GAIL.NS", "GICRE.NS", "GODREJCP.NS",
    "GODREJIND.NS", "GRASIM.NS", "HAVELLS.NS", "HCLTECH.NS", "HDFCLIFE.NS",
    "HEROMOTOCO.NS", "HINDPETRO.NS", "HINDUNILVR.NS", "IOC.NS", "INDIGO.NS",
    "INDUSINDBK.NS", "INFY.NS", "ITC.NS", "JINDALSTEL.NS", "JSWSTEEL.NS",
    "JUBLFOOD.NS", "KOTAKBANK.NS", "LICI.NS", "LT.NS", "LUPIN.NS",
    "M&M.NS", "MGL.NS", "MOTILALOFS.NS", "MRF.NS", "MUTHOOTFIN.NS",
    "NAM-INDIA.NS", "NATIONALUM.NS", "NAUKRI.NS", "NESTLEIND.NS", "NMDC.NS",
    "NTPC.NS", "ONGC.NS", "PEL.NS", "PFC.NS", "PIDILITIND.NS",
    "PNB.NS", "POWERGRID.NS", "PVRINOX.NS", "RAMCOCEM.NS", "RBLBANK.NS",
    "RECLTD.NS", "RELIANCE.NS", "SBIN.NS", "SIEMENS.NS", "SUNPHARMA.NS",
    "SUNTV.NS", "TATAMOTORS.NS", "TATAPOWER.NS", "TATASTEEL.NS", "TCS.NS",
    "TECHM.NS", "TITAN.NS", "TVSMOTOR.NS", "UBL.NS", "UNIONBANK.NS",
    "ULTRACEMCO.NS", "VEDL.NS", "VOLTAS.NS", "WIPRO.NS", "YESBANK.NS",
    "ZEEL.NS", "ZYDUSLIFE.NS", "ADANIPORTS.NS", "ADANIGREEN.NS", "ADANITRANS.NS",
    "AMBUJACEM.NS", "APOLLOTYRE.NS", "ASIANPAINT.NS", "AUROPHARMA.NS", "AXISBANK.NS",
    "BAJAJ-AUTO.NS", "BAJFINANCE.NS", "BANKBARODA.NS", "BHEL.NS", "BIOCON.NS",
    "BOSCHLTD.NS", "BPCL.NS", "BRITANNIA.NS", "CIPLA.NS", "COALINDIA.NS",
    "DABUR.NS", "DLF.NS", "DRREDDY.NS", "EICHERMOT.NS", "ESCORTS.NS",
    "EXIDEIND.NS", "GAIL.NS", "GICRE.NS", "GODREJCP.NS", "GRASIM.NS",
    "HAVELLS.NS", "HCLTECH.NS", "HDFCLIFE.NS", "HEROMOTOCO.NS", "HINDALCO.NS",
    "HINDPETRO.NS", "HINDUNILVR.NS", "IOC.NS", "INDIGO.NS", "INDUSINDBK.NS",
    "INFY.NS", "ITC.NS", "JINDALSTEL.NS", "JSWSTEEL.NS", "KOTAKBANK.NS",
    "LICI.NS", "LT.NS", "LUPIN.NS", "M&M.NS", "MARUTI.NS", "MOTILALOFS.NS",
    "MRF.NS", "NESTLEIND.NS", "NTPC.NS", "ONGC.NS", "PFC.NS", "PIDILITIND.NS",
    "PNB.NS", "POWERGRID.NS", "PVRINOX.NS", "RECLTD.NS", "RELIANCE.NS",
    "SBIN.NS", "SHREECEM.NS", "SIEMENS.NS", "SUNPHARMA.NS", "SUNTV.NS",
    "TATAMOTORS.NS", "TATAPOWER.NS", "TATASTEEL.NS", "TCS.NS", "TECHM.NS",
    "TITAN.NS", "TVSMOTOR.NS", "UBL.NS", "ULTRACEMCO.NS", "UNIONBANK.NS",
    "UPL.NS", "VEDL.NS", "VOLTAS.NS", "WIPRO.NS", "YESBANK.NS", "ZEEL.NS",
    "ZYDUSLIFE.NS", "AJANTPHARM.NS", "ALEMBICLTD.NS", "AMARAJABAT.NS",
    "APLLTD.NS", "BAJAJHLDNG.NS", "BSE.NS", "COLPAL.NS", "CROMPTON.NS",
    "DELTACORP.NS", "DIXON.NS", "EQUITASBNK.NS", "FSL.NS", "GLENMARK.NS",
    "GUJGASLTD.NS", "HONAUT.NS", "IBULHSGFIN.NS", "ICICIGI.NS", "ICICIPRULI.NS",
    "IDBI.NS", "IDFCFIRSTB.NS", "IDFC.NS", "INDIAMART.NS", "INDHOTEL.NS",
    "IRCTC.NS", "L&TFH.NS", "LICHSGFIN.NS", "LICI.NS", "M&MFIN.NS",
    "MANAPPURAM.NS", "METROPOLIS.NS", "MINDTREE.NS", "MPHASIS.NS", "MRPL.NS",
    "NAUKRI.NS", "NMDC.NS", "NTPC.NS", "OFSS.NS", "PAGEIND.NS",
    "PETRONET.NS", "POLYCAB.NS", "PUNJABCHEM.NS", "QUESS.NS", "RBLBANK.NS",
    "RECLTD.NS", "SAIL.NS", "SBILIFE.NS", "SHARDACROP.NS", "SIEMENS.NS",
    "SONACOMS.NS", "SRF.NS", "SUNTV.NS", "TATACONSUM.NS", "TATAELXSI.NS",
    "TECHM.NS", "TIDEWATER.NS", "TVSMOTOR.NS", "UJJIVAN.NS", "UNIONBANK.NS",
    "UPL.NS", "VBL.NS", "VGUARD.NS", "WABCOINDIA.NS", "WHIRLPOOL.NS",
    "ZOMATO.NS"
]

# Remove any duplicates
tickers = list(set(tickers))

# Loop through each ticker and fetch the data.
for ticker in tickers:
    print(f"Fetching data for {ticker}...")
    try:
        # Download historical data for last 5 years.
        stock_data = yf.download(ticker, period = "5y")

        # Check if the dataframe is empty
        if stock_data.empty:
            print(f"No data found for {ticker}, skipping.")
            continue

        # Reset the index to turn the 'Date' index into a column
        stock_data.reset_index(inplace = True)

        # Add a 'ticker' column to identify the stock
        stock_data['ticker'] = ticker

        # Define the output file path
        file_path = os.path.join(data_dir, f"{ticker}_history.csv")

        # Save the DataFrame to a CSV file
        stock_data.to_csv(file_path, index = False)

        print(f"Successfully saved data for {ticker} to {file_path}")

    except Exception as e:
        print(f"Failed to fetch data for {ticker}. Error: {e}")

print("Data ingestion complete.")
print(f"Total tickers processed: {len(tickers)}")