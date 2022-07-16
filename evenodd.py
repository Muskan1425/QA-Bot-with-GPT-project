import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import streamlit as st  

st.title('Python program to check if the input number is odd or even.')
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
st.image('https://thumbs.dreamstime.com/z/titanic-iceberg-original-oil-painting-ocean-night-canvas-full-moon-stars-modern-impressionism-200487951.jpg')
  
def func(num):
     if num%2 == 0:
        return "Even"
     else:
        return "Odd"

df['OddEvenAge'] = df.loc[:,'Age'].apply(func)
df