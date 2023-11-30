import streamlit as st
import pandas as pd

github_url = 'https://github.com/Mustafatekin96/mustafatekin/blob/441c75177f62f6514c836a915076183ce4130961/makine%20saat-eyl%C3%BCl-ekim.xlsx'

df = pd.read_csv(github_url)
