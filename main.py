import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search of Happiness")

options = ["happiness", "gdp", "life expectancy",
            "freedom to make life choices", "generosity", "corruption"]
default_option = 1

x_option = st.selectbox("Select the data for the X-axis",
                        options, index=default_option)
y_option = st.selectbox("Select the data for the Y-axis",
                        options, index=default_option)
st.write("(Note that a lower 'corruption' score indicates more corruption, "
         "whereas a higher score indicates less corruption)")

x_option_underscore = x_option.replace(" ", "_")
y_option_underscore = y_option.replace(" ", "_")

df = pd.read_csv("happy.csv")
x_data = df[x_option_underscore]
y_data = df[y_option_underscore]

st.subheader(f"{x_option} and {y_option}".title())
figure = px.scatter(x=x_data, y=y_data,
                    labels={"x": x_option, "y": y_option})
st.plotly_chart(figure)
