import streamlit as st
from send_email import send_email
import pandas

topic_df = pandas.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address:")
    option = st.selectbox('What topic do you want to discuss?', topic_df["topic"])
    raw_message = st.text_area("Type your message here:")
    message = f"""\
Subject: New email from Company Web.

From: {user_email}
Topic: {option}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully!")