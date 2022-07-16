import numpy as np  
import pandas as pd  
import streamlit as st  
import matplotlib.pyplot as plt
import plotly.express as px 

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

survivedones = (df['Survived']==1).sum()
not_survivedones = (df['Survived']==0).sum()

df = pd.DataFrame({'index': ['survivedones','not_survivedones'],'value' : [survivedones,not_survivedones]}).sort_index('index')
st.bar_chart(df,width=0)