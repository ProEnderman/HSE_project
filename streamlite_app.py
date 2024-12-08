import streamlit as st
from PIL import Image
import pandas as pd



st.header("Leon Kuligin 241-1 Python Project")

st.text(open("/Users/leonkul/projects/python/Session/Description.txt").read())

st.dataframe(pd.read_csv("/Users/leonkul/projects/python/Session/first_10_rows.csv"))

st.text(open("/Users/leonkul/projects/python/Session/text2.txt").read())

st.dataframe(pd.read_csv("/Users/leonkul/projects/python/Session/1.csv"))

st.text(open("/Users/leonkul/projects/python/Session/text3.txt").read())

st.dataframe(pd.read_csv("/Users/leonkul/projects/python/Session/2.csv"))

st.text(open("/Users/leonkul/projects/python/Session/text4.txt").read())

img = Image.open("/Users/leonkul/projects/python/Session/graph1.png")

img = img.resize((1400, 1000), Image.Resampling.LANCZOS)

st.image(img, caption="Bar chart", use_container_width=True)


st.text(open("/Users/leonkul/projects/python/Session/text5.txt").read())

img = Image.open("/Users/leonkul/projects/python/Session/graph2.png")


st.image(img, caption="Pie chart", use_container_width=True)

st.dataframe(pd.read_csv("/Users/leonkul/projects/python/Session/3.csv"))

st.text(open("/Users/leonkul/projects/python/Session/text6.txt").read())

img = Image.open("/Users/leonkul/projects/python/Session/graph3.png")


st.image(img, caption="Combo chart", use_container_width=True)

st.text(open("/Users/leonkul/projects/python/Session/text7..txt").read())

img = Image.open("/Users/leonkul/projects/python/Session/graph4.png")


st.image(img, caption="Scatter plot", use_container_width=True)

st.text(open("/Users/leonkul/projects/python/Session/text8.txt").read())

img = Image.open("/Users/leonkul/projects/python/Session/graph5.png")


st.image(img, caption="Line graph", use_container_width=True)

st.text(open("/Users/leonkul/projects/python/Session/text9.txt").read())

st.dataframe(pd.read_csv("/Users/leonkul/projects/python/Session/4.csv"))

st.text(open("/Users/leonkul/projects/python/Session/text10.txt").read())

img = Image.open("/Users/leonkul/projects/python/Session/graph6.png")


st.image(img, caption="Line Graph", use_container_width=True)

st.text("2.A-tier:")

img = Image.open("/Users/leonkul/projects/python/Session/graph7.png")


st.image(img, caption="Line Graph", use_container_width=True)

st.text("3.B-tier:")

img = Image.open("/Users/leonkul/projects/python/Session/graph8.png")


st.image(img, caption="Line Graph", use_container_width=True)

st.text("4.C-tier:")

img = Image.open("/Users/leonkul/projects/python/Session/graph9.png")


st.image(img, caption="Line Graph", use_container_width=True)

st.text("5.D-tier:")

img = Image.open("/Users/leonkul/projects/python/Session/graph10.png")


st.image(img, caption="Line Graph", use_container_width=True)

st.text(open("/Users/leonkul/projects/python/Session/text11.txt").read())


st.dataframe(pd.read_csv("/Users/leonkul/projects/python/Session/5.csv"))


st.text(open("/Users/leonkul/projects/python/Session/text12.txt").read())


img = Image.open("/Users/leonkul/projects/python/Session/graph11.png")


st.image(img, caption="Bar Chart", use_container_width=True)


st.text("2.A-tier:")

img = Image.open("/Users/leonkul/projects/python/Session/graph12.png")


st.image(img, caption="Bar Chart", use_container_width=True)

st.text("3.B-tier:")

img = Image.open("/Users/leonkul/projects/python/Session/graph13.png")


st.image(img, caption="Bar Chart", use_container_width=True)

st.text("4.C-tier:")

img = Image.open("/Users/leonkul/projects/python/Session/graph14.png")


st.image(img, caption="Bar Chart", use_container_width=True)


st.text("5.D-tier:")

img = Image.open("/Users/leonkul/projects/python/Session/graph15.png")


st.image(img, caption="Bar Chart", use_container_width=True)

st.text(open("/Users/leonkul/projects/python/Session/text13.txt").read())

st.header("My Hypothesis")

st.text(open("/Users/leonkul/projects/python/Session/text14.txt").read())

st.text(open("/Users/leonkul/projects/python/Session/text15.txt").read())


st.dataframe(pd.read_csv("/Users/leonkul/projects/python/Session/6.csv"))

st.text(open("/Users/leonkul/projects/python/Session/text16.txt").read())


st.dataframe(pd.read_csv("/Users/leonkul/projects/python/Session/7.csv"))

st.text(open("/Users/leonkul/projects/python/Session/text17.txt").read())


st.dataframe(pd.read_csv("/Users/leonkul/projects/python/Session/8.csv"))

st.text(open("/Users/leonkul/projects/python/Session/text18.txt").read())


st.dataframe(pd.read_csv("/Users/leonkul/projects/python/Session/9.csv"))

st.text(open("/Users/leonkul/projects/python/Session/text19.txt").read())


st.dataframe(pd.read_csv("/Users/leonkul/projects/python/Session/10.csv"))

st.text(open("/Users/leonkul/projects/python/Session/text20.txt").read())


img = Image.open("/Users/leonkul/projects/python/Session/graph16.png")


st.image(img, caption="Scatter Plot", use_container_width=True)

st.text(open("/Users/leonkul/projects/python/Session/text21.txt").read())

img = Image.open("/Users/leonkul/projects/python/Session/heatmap.png")


st.image(img, caption="HeatMap", use_container_width=True)

st.text(open("/Users/leonkul/projects/python/Session/text22.txt").read())


st.dataframe(pd.read_csv("/Users/leonkul/projects/python/Session/11.csv"))

st.text(open("/Users/leonkul/projects/python/Session/text23.txt").read())


st.dataframe(pd.read_csv("/Users/leonkul/projects/python/Session/12.csv"))

st.text(open("/Users/leonkul/projects/python/Session/text24.txt").read())