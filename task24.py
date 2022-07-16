import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import streamlit as st  
import matplotlib.pyplot as plt
import plotly.express as px 

def main():  

  df1 = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
  st.dataframe(df1)
 
  fig = plt.figure()
  df1["Survived"].value_counts().plot(kind = "bar")
  st.pyplot(fig)
main()

def main(): 
 chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])
st.bar_chart(chart_data)
main()


def main():  

  df2 = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
  st.dataframe(df2) 

  fig2= px.pie(df2, values='values', names='Pclass')
  fig2.show()
main() 