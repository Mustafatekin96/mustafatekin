import streamlit as st
import pandas as pd

# Streamlit uygulamasını başlat
st.title("Excel Okuma Uygulaması")

# Dosya seçme aracı ekleyin
uploaded_file = st.file_uploader("Excel dosyanızı yükleyin", type=["csv"])

# Dosya yüklendiyse
if uploaded_file is not None:
    # Excel dosyasını oku
    df = pd.read_csv(uploaded_file)

    # Veri çerçevesini görüntüle
    st.write("Yüklenen Excel Dosyası:")
    df = pd.DataFrame(df)
    st.write(df)


