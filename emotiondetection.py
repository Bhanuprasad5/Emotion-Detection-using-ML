import pickle

import pandas as pd
import sklearn
from PIL import Image


import streamlit as st



image= Image.open(r"573326-innomatics_research_labs_logo.png")
st.image(image)
# st.image(r"573326-innomatics_research_labs_logo.png")
model = pickle.load(open(r"emotion_detection.pkl","rb"))

text = st.text_input("Enter the Text :")





if st.button("Submit"):
    
    
    pred = model.predict([text])[0]
    st.write("The Email is : ",pred)
    st.image(r"joy emoji.jpeg",width=200)
