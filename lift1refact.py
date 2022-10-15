# Calorie calculator for maintenance/bulk/cut
# Outline for calorie calulator -- 
# Enter Name, Age, M/F, Weight, Height
# Find maintenance (BMR)
# Choose bulk/cut
# Maintenance for 2 weeks, +100/weekly for bulk, -100/weekly for cut

# Step 1: Find Basal Metabolic Rate for base calory need

import streamlit as st

st.title('Calory Calculator')
a = (input("Enter your bodyweight (rounded off) in kgs: "))
b = (input("Enter your height in cms: "))
c = (input("Enter your age in years: "))
d = (input("Do you have a: A. Sedentary life B. Exercise 1-3 days C. Exercise 4-5 days D. Intense exercise 4-5 days E. Intense exercise 6-7 days F. Daily exercise/physical job: [Answer with A/B/C/D/E/F] "))
BMR = print("Your maintenance is: " + str(10*int(a) + (6.25*float(b) - 5*int(c))))



