import streamlit as st
import pandas as pd

github_raw_url = 'https://github.com/Mustafatekin96/mustafatekin/blob/5a2d820e3f9649f163350d9eabad035f487872c4/.devcontainer/machine.csv'


with st.echo():
    try:
        df = pd.read_csv(github_raw_url)
    except Exception as e:
        st.error(f"An error occurred: {e}")
df = df.dropna()
st.dataframe(df.head())
