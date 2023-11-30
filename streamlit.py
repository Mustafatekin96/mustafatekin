import streamlit as st
import pandas as pd

df = pd.read_excel("makine saat-eylül-ekim.xlsx")
st.dataframe(df.head(5))
