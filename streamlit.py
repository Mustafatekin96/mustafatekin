import streamlit as st


df = pd.read_excel("mustafatekin/makine saat-eylül-ekim.xlsx")
st.dataframe(df.head(5))
