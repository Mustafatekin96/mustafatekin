import streamlit as st
import pandas as pd

github_url = 'https://github.com/Mustafatekin96/mustafatekin/blob/13c37485be03ad40b3f4ad1ca4408171bfe2c90f/makine%20saat-eyl%C3%BCl-ekim.csv'

df = pd.read_csv(github_url)
