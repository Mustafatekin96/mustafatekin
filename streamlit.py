import streamlit as st
import pandas as pd

# Streamlit başlığı
st.title("Veri Tabanlı Tahmin Uygulaması")

# Veri girişleri için text alanları oluşturma
st.sidebar.header("Veri Girişleri")
input_1 = st.sidebar.text_input("Giriş 1", "Değer 1")
input_2 = st.sidebar.text_input("Giriş 2", "Değer 2")
input_3 = st.sidebar.text_input("Giriş 3", "Değer 3")
input_4 = st.sidebar.text_input("Giriş 4", "Değer 4")
input_5 = st.sidebar.text_input("Giriş 5", "Değer 5")

# Düğmeye tıklanınca tahmin yapma işlemi
if st.sidebar.button("Tahmin Yap"):
    # Gerçek bir model kullanmak isterseniz, modeli yükleyip tahmin işlemini burada gerçekleştirebilirsiniz
    # Örnek basit tahmin:
    prediction = "Tahmin Yok"
    if input_1 and input_2 and input_3 and input_4 and input_5:
        prediction = "Örnek Tahmin Sonucu"

    sum = int(input_1) + int(input_2)+ int(input_3)

    # Tahmin sonucunu gösterme
    st.write("Tahmin Sonucu:")
    st.write(sum)
