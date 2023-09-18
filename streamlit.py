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




veri_listesi = ["Seçenek 1", "Seçenek 2", "Seçenek 3", "Seçenek 4"]

# Streamlit uygulama başlatma
st.title("ComboBox Örneği")
st.write("Lütfen bir seçenek seçin:")

# ComboBox (selectbox) oluşturma
secilen_veri = st.selectbox("Seçenekler", veri_listesi)

# Seçilen veriyi gösterme
st.write("Seçilen veri:", secilen_veri)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Örnek bir Pandas DataFrame oluşturma
veri = {
    'Tarih': ['2023-09-01', '2023-09-02', '2023-09-03', '2023-09-04'],
    'Değer': [10, 20, 15, 30]
}

df = pd.DataFrame(veri)

# Streamlit uygulama başlatma
st.title("Grafik Gösterme Örneği")

# Düğmeye tıklanıp tıklanmadığını kontrol etmek için bir boolean değişken
tiklandi_mi = st.button("Grafiği Göster")

# Eğer düğmeye tıklanırsa
if tiklandi_mi:
    # Verileri kullanarak bir çizgi grafiği oluşturma
    fig, ax = plt.subplots()
    ax.plot(df['Tarih'], df['Değer'], marker='o')
    ax.set_xlabel('Tarih')
    ax.set_ylabel('Değer')
    ax.set_title('Örnek Çizgi Grafiği')

    # Grafiği gösterme
    st.pyplot(fig)






