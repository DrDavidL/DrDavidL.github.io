
import yfinance as yf
import streamlit as st
from streamlit_pages.streamlit_pages import MultiPage


 

# multiple pages test

def home():
    st.write("Welcome to home page")
    if st.button("Click Home"):
        st.write("Welcome to home page")


def about():
    st.write("Welcome to about page")
    if st.button("Click about"):
        st.write("Welcome to About page")


def contact():
    st.write("Welcome to contact page")
    if st.button("Click Contact"):
        st.write("Welcome to contact page")


# call app class object
app = MultiPage()
# Add pages
app.add_page("Home",home)
app.add_page("About",about)
app.add_page("Contact",contact)
app.run()

# end multiple pages test

st.write("""
# Demo Stock Price App - Enter stock of interest for demonstration purposes here.
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = st.text_input('Enter your ticker symbol!')


st.write("""
# Before we actually create the graphs for your stock, let's experiment with your BMI!
""") 

if len(tickerSymbol) != 0:
    

    heightstr = st.text_input('Enter your height in inches:')
    weightstr = st.text_input('Enter your weight in pounds:')
    
    if len(weightstr) != 0 and len(heightstr) !=0:

        height = float(heightstr)
        weight = float(weightstr)

        weightkg = weight * 0.453592
        heightcm = height * 2.54

        bmi = weightkg / (heightcm/100)**2

        st.write("# Your BMI is:", round(bmi,1))

        # print(round(bmi,1))



        #get data on this ticker
        tickerData = yf.Ticker(tickerSymbol)
        #get the historical prices for this ticker
        tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
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