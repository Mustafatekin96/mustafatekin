import streamlit as st
import pandas as pd

github_raw_url = 'https://github.com/Mustafatekin96/mustafatekin/blob/e71f0592998c28cbcd645aa1e2de328d34a3d22b/customers.csv'

df = pd.read_csv(github_raw_url, sep='\t')  # Sütunlar sekme (tab) ile ayrılmış

st.dataframe(df)
