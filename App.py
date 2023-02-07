import streamlit as st
import pandas as pd
import numpy as np
import pyrebase



# config = {
#   "apiKey": "AIzaSyCGumwxWqlmTRXsJfzEr6p_YxGhZhW7btE",
#   "authDomain": "smdapp-167f1.firebaseapp.com",
#   "databaseURL": "https://smdapp-167f1
#   "storageBucket": "smdapp-167f1.appspot.com",
#   "messagingSenderId": "9839005187",
#   "appId": "1:9839005187:web:1de5376366353fe8c48836"
# }

config = {
  "apiKey": "AIzaSyAtMjemWFKTd8hR3A_UfdFiaFDZB9Am6VA",
  "authDomain": "fyp-project-e8411.firebaseapp.com",
  "databaseURL" : "https://fyp-project-e8411-default-rtdb.firebaseio.com",
  "projectId": "fyp-project-e8411",
  "storageBucket": "fyp-project-e8411.appspot.com",
  "messagingSenderId": "308468395801",
  "happId": "1:308468395801:web:e8120b9a9bf39d915f9f88"
};


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db = firebase.database()


st.title('Suspicious Activity Records')

st.markdown('''
<style>
    body{
        background: white;
    }
.row-widget, .stButton{
   

}
 .stButton > button{
    width : 50%;
    background: lightblue;
    font-size: 22px;
    box-shadow: 0px 0px 10px lightgreen;
    display: block;
    margin: 0 auto;
    border: none
 }
 .css-1p0pxej, .e1tzin5v3{
    padding: 5px;
    box-shadow: 0px 0px 10px lightgray;
    text-align: center;
    border-radius: 5px;
    
 }
 #suspicious-activity-records{
    
    text-align: center;
    text-shadow: 0px 2px 5px lightgray;
    margin: 0;
 }
 
 footer{
    visibility: hidden;
 }
</style>
''',unsafe_allow_html=True )

def loadData():
    data = db.child("imagesData").get()
    for d in data.each():
        with st.container():
            key = d.key()
            values = d.val()
            name = values["name"]
            date = values["date"]
            time = values["time"]
            image_url = storage.child(key+".jpg").get_url(None)
            st.write("Name: "+name)
            st.write("Date: "+date)
            st.write("Time: "+time)
            st.image(image_url)
            args = (key,name,date,time)
            
          
        
if st.button('Fetch Records'):
    loadData()
