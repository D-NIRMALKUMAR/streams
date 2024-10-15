import streamlit as st

# Set the title of the app
st.title("Feedback App")

# Create a text input for the user to enter feedback
user_input = st.text_input("Please provide your feedback:")

# Create a button that, when clicked, shows the feedback
if st.button("Submit Feedback"):
    if user_input:
        st.success(f"Thank you for your feedback: '{user_input}'")
    else:
        st.error("Please enter your feedback before submitting.")
