import streamlit as st
import yfinance as yf


from multipage import MultiPage
from pages.bmiapp import bmiapp
from pages.stockapp import stockapp
from pages.primes import primes



app = MultiPage()

# Add all your pages here
app.add_page("BMI Calculator", bmiapp)
app.add_page("Stock Chart", stockapp)
app.add_page("Prime Generator", primes)

# Add the main content
st.title("Python on the Web - Welcome FSM!")
st.write('*These are examples of python pushed to the web. More to come!*')

app.run()
