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
st.write("(Note that a lower 'corruption' score indicates more corruption,"
         "whereas a higher score indicates less corruption)")

x_option = x_option.replace(" ", "_")
y_option = y_option.replace(" ", "_")

df = pd.read_csv("happy.csv")
x_data = df[x_option]
y_data = df[y_option]

figure = px.scatter(x=x_data, y=y_data,
                    labels={"x": x_option.replace("_", " "), "y": y_option.replace("_", " ")})
st.plotly_chart(figure)
