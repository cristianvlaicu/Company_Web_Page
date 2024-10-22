    # Vamos a crear una página web de una empresa con múltiples páginas dentro, Home y otra que sea un formulario que rellene el usuario y nos llegue a nosotros un email como ese formulario.

import streamlit as st
import pandas

# Set webpage layout to wide
st.set_page_config(layout="wide")

# Add a header and some other text
st.markdown(
    """
    <h1 style="text-align: center;">TechSolutions: Simplifying technology for you.</h3>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <h5 style="text-align: justify;">TechSolutions is a dynamic and innovative technology company dedicated to providing cutting-edge technology solutions for businesses and individuals. Our team of experts specializes in custom software development, intuitive mobile applications, and robust cybersecurity solutions. We are passionate about helping our clients harness the power of technology to optimize their operations, drive growth, and achieve their goals. Whether you need a mobile app to connect with your customers, management software to streamline your processes, or a cybersecurity strategy to protect your data, TechSolutions has the perfect solution for you. At TechSolutions, we believe that technology should be accessible, intuitive, and above all, useful.</h3>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <h3 style="text-align: center;">Our Team:</h3>
    """, unsafe_allow_html=True)


# Prepare the columns
col1, col2, col3 = st.columns(3)

# Make a dataframe with the company members
df = pandas.read_csv("data.csv")  #here we don't use 'set=', cause by default is set by ','; like in data.csv.

# Add content to the first column
with col1:
    # Iterate over only the first four rows
    for index, row in df[:4].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])

# Add content to the second column
with col2:
    # Iterate over rows 4 to 7
    for index, row in df[4:8].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])


with col3:
    # Iterate over rows 4 to 7
    for index, row in df[8:].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])