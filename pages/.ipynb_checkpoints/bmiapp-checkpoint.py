import streamlit as st

def bmiapp():
    st.title("BMI Calculator")
    st.write('*Use pounds and inches!!!*')
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