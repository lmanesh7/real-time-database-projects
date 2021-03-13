#Code_Author = lakshman_manesh

import streamlit as st
import pandas as pd
import pyrebase


config = {
    "apiKey": "AIzaSyBz9K9JuS4R6xIJrkVCA6kJ6BcuO_kx9aI",
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

user = db.child("water level").get()
us = user.val()
keys_list = []
vals_list = []
for i in us.values():
    # print(i)
    for j in i:
        keys_list.append(j)
        vals_list.append(i[j])
#df = pd.DataFrame({"water level": keys_list, "Time": vals_list})
#print(keys_list)
#print(vals_list)
daylist = []
yearlist = []
motorlist = []
for i in vals_list:
        daylist.append(i[0])
        yearlist.append(i[1])
        motorlist.append(i[2])


#print(daylist)
#print(yearlist)

df = pd.DataFrame({"water level":keys_list,"time":daylist,"year":yearlist,"motor state":motorlist})
st.title("water level monitoring system")
k=keys_list[-1]
st.write("Water Level: %s" %k)
st.write("Motor state: %s" %motorlist[-1])
if st.checkbox("show entire database"):
    st.write(df)
#option = st.sidebar.selectbox("select one", [x for x in range(100)])
latest = st.empty()
k=(int(k)/30)*100
st.write("water level percentage %f:" %(k))
bar = st.progress(int(k))
#st.write("Designed and Developed by lakshman manesh")
#designed and developed by lakshman_manesh
