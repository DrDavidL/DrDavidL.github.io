import streamlit as st
import yfinance as yf
from datetime import date
from dateutil.relativedelta import *


def stockapp():
    st.title("StockChart Example")
    st.write('*Enter your stock symbol and see the magic!*')
            #get data on this ticker
    tickerSymbol = st.text_input('Enter your ticker symbol!')
    tickerData = yf.Ticker(tickerSymbol)
        #get the historical prices for this ticker
    if len(tickerSymbol) != 0:
        now = str(date.today())
        starter = str(date.today() + relativedelta(years=-2))
        #starter = now + dateutil.relativedelta.relativedelta(years=-2)
        #tickerDf = tickerData.history(period='1d', start='2019-5-31', end=now)
        tickerDf = tickerData.history(period='1d', start=starter, end=now)
            # Open	High	Low	Close	Volume	Dividends	Stock Splits

            # st.line_chart(tickerDf.Close)
            # st.line_chart(tickerDf.Volume)

        st.write("""
            ## Closing Price
            """)
        st.line_chart(tickerDf.Close)
        st.write("""
            ## Volume
            """)
        st.line_chart(tickerDf.Volume)