import streamlit as st
import pandas as pd
df = pd.read_csv(, sep=';')  # Sütunlar sekme (tab) ile ayrılmış

# Multiselect bileşeni
selected_values = st.multiselect('Multiselect', [1, 2, 3])

# Button bileşeni
button_clicked = st.button('Hit me')

# Seçilen değerleri yazdırma
st.write('Selected Values:', selected_values)

# Butona tıklanıp tıklanmadığını kontrol etme
if button_clicked:
    st.write('Button Clicked!')
