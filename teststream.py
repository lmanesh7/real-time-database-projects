#author="lakshman_manesh"

import streamlit as st
import pandas as pd
import datetime as dt
import plotly.graph_objects as go


df = pd.read_csv("sensor.csv")

#df1 = df.drop(['unnamed'],axis=1)
 
st.title(" " "Manesh's Room Humidity Monitoring!" " ")

st.write("Humidity level chart")
st.line_chart(df['y'])
t = df['y'].tail(1)
'''fig = go.Figure(y=df['y'])
fig.update_layout(autosize=True,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))'''
#st.plotly_chart(t)


st.write("Entire HighLighted DB")
st.dataframe(df.style.highlight_max(axis=0))
l=[0,10,20,25,40,50,70,75,95]
st.write("You can check some border equal values using the frequently checked values below")
n=st.radio("frequently checked values",l)
if n in l:
    st.write("Your selected value list is here!")
    st.write(df.query("y==@n"))

min = st.sidebar.number_input("From level",min_value=10)
max = st.sidebar.number_input("To level",min_value=10,value=95)
if min>max:
    st.error("please enter a valid range")
else:
    st.write("Your range query result is here!")
    st.write(df.query("@min<=y<=@max"))

x = dt.datetime.now().strftime('%c')
df['z'] = pd.to_datetime(df['z'],format="%d-%m-%Y")

d3 = st.date_input("range",[dt.date(2021,1,9) , dt.date(2021,1,9)])
#st.write(d3)
try:
   min1 = d3[0]
   max1 = d3[1]
   if max1>=min1:
       st.write(df.query("@min1<=z<=@max1"))
   else:
       st.write("To date is shorter than from date ")
except IndexError:
   st.write("Enter two range dates")

pic ="PSX_20201122_184952.jpg"

st.image(pic)


st.write(" " " Designed and developed by lakshman_manesh" " ")
