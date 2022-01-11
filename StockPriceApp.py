import yfinance as yf
import pandas as pd
import streamlit as st

st.write("""
# Stock Price App

Stock closing price and volume of **google**!
""")

# The Ticker interface is used to setup a recurring interrupt to repeatedly call a function at a specified rate.
# When a company issues securities to the public marketplace, it selects an available ticker symbol for its 
#     securities that investors and traders use to transact orders.

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='id',start='2010-5-31',end='2020-5-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)