import streamlit as st
from PIL import Image
import pandas as pd

st.header("Leon Kuligin 241-1 Python Project")

st.text(open("Description.txt").read())

st.dataframe(pd.read_csv("first_10_rows.csv"))

st.text(open("text2.txt").read())

st.dataframe(pd.read_csv("1.csv"))

st.text(open("text3.txt").read())

st.dataframe(pd.read_csv("2.csv"))

st.text(open("text4.txt").read())

img = Image.open("graph1.png")
img = img.resize((1400, 1000), Image.Resampling.LANCZOS)
st.image(img, caption="Bar chart", use_container_width=True)

st.text(open("text5.txt").read())

img = Image.open("graph2.png")
st.image(img, caption="Pie chart", use_container_width=True)

st.dataframe(pd.read_csv("3.csv"))

st.text(open("text6.txt").read())

img = Image.open("graph3.png")
st.image(img, caption="Combo chart", use_container_width=True)

st.text(open("text7.txt").read())

img = Image.open("graph4.png")
st.image(img, caption="Scatter plot", use_container_width=True)

st.text(open("text8.txt").read())

img = Image.open("graph5.png")
st.image(img, caption="Line graph", use_container_width=True)

st.text(open("text9.txt").read())

st.dataframe(pd.read_csv("4.csv"))

st.text(open("text10.txt").read())

img = Image.open("graph6.png")
st.image(img, caption="Line Graph", use_container_width=True)

st.text("2.A-tier:")
img = Image.open("graph7.png")
st.image(img, caption="Line Graph", use_container_width=True)

st.text("3.B-tier:")
img = Image.open("graph8.png")
st.image(img, caption="Line Graph", use_container_width=True)

st.text("4.C-tier:")
img = Image.open("graph9.png")
st.image(img, caption="Line Graph", use_container_width=True)

st.text("5.D-tier:")
img = Image.open("graph10.png")
st.image(img, caption="Line Graph", use_container_width=True)

st.text(open("text11.txt").read())

st.dataframe(pd.read_csv("5.csv"))

st.text(open("text12.txt").read())

img = Image.open("graph11.png")
st.image(img, caption="Bar Chart", use_container_width=True)

st.text("2.A-tier:")
img = Image.open("graph12.png")
st.image(img, caption="Bar Chart", use_container_width=True)

st.text("3.B-tier:")
img = Image.open("graph13.png")
st.image(img, caption="Bar Chart", use_container_width=True)

st.text("4.C-tier:")
img = Image.open("graph14.png")
st.image(img, caption="Bar Chart", use_container_width=True)

st.text("5.D-tier:")
img = Image.open("graph15.png")
st.image(img, caption="Bar Chart", use_container_width=True)

st.text(open("text13.txt").read())

st.header("My Hypothesis")

st.text(open("text14.txt").read())

st.text(open("text15.txt").read())

st.dataframe(pd.read_csv("6.csv"))

st.text(open("text16.txt").read())

st.dataframe(pd.read_csv("7.csv"))

st.text(open("text17.txt").read())

st.dataframe(pd.read_csv("8.csv"))

st.text(open("text18.txt").read())

st.dataframe(pd.read_csv("9.csv"))

st.text(open("text19.txt").read())

st.dataframe(pd.read_csv("10.csv"))

st.text(open("text20.txt").read())

img = Image.open("graph16.png")
st.image(img, caption="Scatter Plot", use_container_width=True)

st.text(open("text21.txt").read())

img = Image.open("heatmap.png")
st.image(img, caption="HeatMap", use_container_width=True)

st.text(open("text22.txt").read())

st.dataframe(pd.read_csv("11.csv"))

st.text(open("text23.txt").read())

st.dataframe(pd.read_csv("12.csv"))

st.text(open("text24.txt").read())