import streamlit as st
import pandas as pd
df = pd.read_csv("https://github.com/Mustafatekin96/mustafatekin/blob/33220848dffb043a8ac372a0876763e9b87b648b/customers.csv", sep=';')  # Sütunlar sekme (tab) ile ayrılmış

# Multiselect bileşeni
selected_values = st.multiselect('Multiselect', [1, 2, 3])

# Button bileşeni
button_clicked = st.button('Hit me')

# Seçilen değerleri yazdırma
st.write('Selected Values:', selected_values)

# Butona tıklanıp tıklanmadığını kontrol etme
if button_clicked:
    st.write('Button Clicked!')
