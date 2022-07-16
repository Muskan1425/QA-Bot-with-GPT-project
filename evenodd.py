import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import streamlit as st 
from PIL import Image 

st.title('Python program to check if the input number is odd or even.')
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
  
def func(num):
     if num%2 == 0:
        return "Even"
     else:
        return "Odd"

df['OddEvenAge'] = df.loc[:,'Age'].apply(func)


image = Image.open('download.jpg')
st.image(image, caption='Titanic image')

df