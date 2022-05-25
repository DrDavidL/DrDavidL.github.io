import streamlit as st

#def isfloat(list):
#    if len(list) == 0:
#        return
#   else:
#        for n in list:
#            try:
#                isok = float(n)
#                except ValueError:
#                    st.write("Please enter numbers only; not other characters.")
    

def bmiapp():
    st.title("BMI Calculator")
    st.write('*Use pounds and inches!!!*')
    heightstr = st.text_input('Step 1. Please enter your height in inches:')
    weightstr = st.text_input('Step 2. Please enter your weight in pounds:')
    

    
    
   # testing = isfloat(inputlist)
   
    if len(heightstr) != 0 and len(weightstr) != 0:
        try:
            heightf = float(heightstr)
        except ValueError:
            st.write("Please enter a numerical value for height.")
            return
        
        try:
            weightf = float(weightstr)
        except ValueError:
            st.write("Please enter a numerical value for weight.")
            return


        if float(heightstr) > 96 or float(heightstr) < 20 or float(weightstr) > 600 or float(weightstr) < 10:
            st.write("Your values are out of range. Please check your inches and pounds!")
        else:



            height = float(heightstr)
            weight = float(weightstr)



            weightkg = weight * 0.453592
            heightcm = height * 2.54

            bmi = weightkg / (heightcm/100)**2

            st.write("# Your BMI is:", round(bmi,1))

        # print(round(bmi,1))