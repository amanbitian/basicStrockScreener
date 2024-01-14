import streamlit as st
import pandas as pd
import yfinance as yf

# Function to get stock data
def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

# Function to screen stocks based on user input
def screen_stocks(stock_data, min_price, max_price, min_volume):
    filtered_stocks = stock_data[
        (stock_data['Close'] >= min_price) &
        (stock_data['Close'] <= max_price) &
        (stock_data['Volume'] >= min_volume)
    ]
    return filtered_stocks

# Streamlit UI
st.title("Stock Screening Application")

# User input for stock symbol, date range, and screening criteria
symbol = st.text_input("Enter Stock Symbol (e.g., AAPL):", "AAPL")
start_date = st.date_input("Start Date:", pd.to_datetime('2022-01-01'))
end_date = st.date_input("End Date:", pd.to_datetime('2023-01-01'))

min_price = st.number_input("Minimum Price:", 0.0)
max_price = st.number_input("Maximum Price:", 1000.0)

min_volume = st.number_input("Minimum Volume:", 0)

# Get stock data
stock_data = get_stock_data(symbol, start_date, end_date)

# Screen stocks based on user input
filtered_stocks = screen_stocks(stock_data, min_price, max_price, min_volume)

# Display filtered stocks
st.subheader("Filtered Stock Data:")
st.write(filtered_stocks)

# You can add more visualizations or information as needed
# For example, a line chart of the stock's closing price
st.subheader("Stock Closing Price Chart:")
st.line_chart(filtered_stocks['Close'])
