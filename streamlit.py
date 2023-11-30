import streamlit as st
import pandas as pd

github_raw_url = 'https://github.com/Mustafatekin96/mustafatekin/blob/5a2d820e3f9649f163350d9eabad035f487872c4/.devcontainer/machine.csv'


df = pd.read_csv(github_raw_url, sep=',') 
st.dataframe(df.head())
