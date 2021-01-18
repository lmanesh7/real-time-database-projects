import streamlit as st
import pandas as pd
import pyrebase
import datetime as dt
from timezones import *
from pytz import timezone
import os
from dotenv import *

load_dotenv(dotenv_path='/.env')

config = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": "test-a9823.firebaseapp.com",
    "databaseURL": "https://test-a9823-default-rtdb.firebaseio.com",
    "projectId": "test-a9823",
    "storageBucket": "test-a9823.appspot.com",
    "messagingSenderId": "1097818977650",
    "appId": "1:1097818977650:web:85b5d03d168fe3db7259eb",
    "measurementId": "G-KN10KC82JL"

}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
k = "lakshman_manesh"
v="11-01-2021"


user = db.child("login").get()
us = user.val()
keys_list =[]
vals_list = []
for i in us.values():
    #print(i)
    for j in i:
        keys_list.append(j)
        t= i[j]
        vals_list.append(t)
df = pd.DataFrame({"User":keys_list,"Login Time":vals_list})
df['LoginUTC'] = pd.to_datetime(df['Login Time'])
df['loginAsia/Kolkata']=df['LoginUTC'].dt.tz_localize('Asia/Kolkata')



keys = keys_list[len(keys_list)-1:len(keys_list)-6:-1]
vals = vals_list[len(vals_list)-1:len(vals_list)-6:-1]


st.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Lakshman\'s face recognition security login data</p>', unsafe_allow_html=True)
#st.write(" " " Lakshman's face recognition security login data" " ")
st.write("Recent five logins")
st.write("user:" +"\t"+ "date")
for (i,j) in zip(keys,vals):
        st.write(i+":"+j)
      
st.write(df)


d3 = st.date_input("Enter start  and end date range ",[dt.datetime.now(),dt.datetime.now()])
#st.write(d3)

try:
   min1 = d3[0]
   max1 = d3[1]
   if max1>=min1:
         st.write(df.query("@min1<=LoginUTC<=@max1"))
   else:
         st.write("To date is shorter than from date ")
except IndexError:
    st.write("Please enter two ranges")
