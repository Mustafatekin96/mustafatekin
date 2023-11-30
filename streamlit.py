import streamlit as st
import pandas as pd

github_url = 'https://raw.githubusercontent.com/username/repo/main/data.csv'

# Pandas DataFrame oluşturma
df = pd.read_csv(github_url)
