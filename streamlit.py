import streamlit as st
import pandas as pd

# Streamlit uygulamasını başlat
st.title("Excel Okuma Uygulaması")

# Dosya seçme aracı ekleyin
uploaded_file = st.file_uploader("Excel dosyanızı yükleyin", type=["xlsx", "xls"])

# Dosya yüklendiyse
if uploaded_file is not None:
    # Excel dosyasını oku
    df = pd.read_excel(uploaded_file)

    # Veri çerçevesini görüntüle
    st.write("Yüklenen Excel Dosyası:")
    st.write(df)
