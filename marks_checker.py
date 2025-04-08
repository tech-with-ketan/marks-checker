# filename: marks_checker.py

import streamlit as st

st.title("📊 Marks Percentage & Grade Checker")

st.write("Enter your marks below to check your percentage and grade.")

# Inputs
total_marks = st.number_input("Enter total marks of one subject", min_value=1.0)
obtained_marks = st.number_input("Enter how many marks you got in the exam", min_value=0.0)

# Button
if st.button("Calculate"):
    if obtained_marks > total_marks:
        st.error("Obtained marks cannot be more than total marks.")
    else:
        percentage = (obtained_marks / total_marks) * 100
        st.success(f"Your percentage is: {percentage:.2f}%")

        # Grade checker
        if 90 <= percentage <= 100:
            st.info("🎉 Grade: A+")
        elif 80 <= percentage < 90:
            st.info("🎉 Grade: A")
        elif 70 <= percentage < 80:
            st.info("🎉 Grade: B")
        elif 50 <= percentage < 70:
            st.info("🎉 Grade: C")
        elif 33 <= percentage < 50:
            st.info("🎉 Grade: D")
        else:
            st.error("❌ Grade: Fail")
