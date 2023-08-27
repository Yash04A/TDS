#Import streamlit
import streamlit as st

#Set the title of the app
st.title("Find the largest among 3 numbers")

# Get the input from the user
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)
num3 = st.number_input("Enter the third number", value=0)

#Call the function and display the result
largest = max(num1, num2, num3)
st.write(f"The largest number is {largest}")
