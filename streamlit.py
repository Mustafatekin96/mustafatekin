import streamlit as st
import pandas as pd


st.title("Sipariş Oluşturma")

uploaded_file = st.file_uploader("Sipariş Dosyasını Yükleyin", type=["xls"])
uploaded_file1 = st.file_uploader("Kanban Stoklarını yükleyin", type=["xlsx"])

if uploaded_file1 is not None:
    df = pd.read_excel(uploaded_file)
    dfkanban = pd.read_excel(uploaded_file1)
    dfkanban = dfkanban[["KOD", "STOK"]]
    dfkanban = dfkanban.rename(columns={"STOK": "Kanban"})
    df.fillna(0, inplace=True)

    df = pd.merge(df, dfkanban, how="left", left_on="MALZEME", right_on="KOD")
    df = df.drop(columns="KOD")

    df = df.drop(columns="STOK")
    df_melted = pd.melt(df, id_vars=['MALZEME', "KODU VE TANIMI", "Kanban"], var_name='Tarih',
                        value_name='Sipariş Miktarı')

    df = df_melted.sort_values(by=['MALZEME', 'Tarih'])

    df = df[df["Sipariş Miktarı"] != 0]
    df = df[df["MALZEME"] != "TOPL"]

    df = df.dropna(subset=['Sipariş Miktarı'])

    df.fillna(0, inplace=True)
    df = df[df["KODU VE TANIMI"] != "KPG"]

    df = df[df["MALZEME"] != 42199296]
    df = df[df["MALZEME"] != 42074682]
    df = df[df["MALZEME"] != 42290108]
    df = df[df["MALZEME"] != 42186714]

    df = df.reset_index(drop=True)
    df['Ürünler_Alt_Satir'] = df['MALZEME'].shift()
    matching_rows = df['MALZEME'] == df['Ürünler_Alt_Satir']
    df["Kalan"] = 0
    for col in df.index:
        if not matching_rows[col]:
            df.loc[col, "Kalan"] = df.loc[col, "Kanban"] - df.loc[col, "Sipariş Miktarı"]
        else:
            df.loc[col, "Kalan"] = df.loc[col - 1, "Kalan"] - df.loc[col, "Sipariş Miktarı"] if col > 0 else 0
    df.drop(columns="Ürünler_Alt_Satir", inplace=True)

    df.drop(df[df['Kalan'] > 0].index, inplace=True)
    df.fillna(0, inplace=True)
    df.loc[df['Kalan'] < 0, 'Kalan'] *= -1

    df['Ürünler_Alt_Satir'] = df['MALZEME'].shift()
    matching_rows = df['MALZEME'] == df['Ürünler_Alt_Satir']

    for col in df.index:
        if not matching_rows[col]:
            df.loc[col, "Kalan2"] = df.loc[col, "Kalan"]
        else:
            df.loc[col, "Kalan2"] = df.loc[col, "Sipariş Miktarı"]
    df.fillna(0, inplace=True)

    df = df[["MALZEME", "Tarih", "Kalan2"]]

    df = df.rename(columns={"Kalan2": "Sipariş Miktarı"})
    st.write("Yüklenen Excel Dosyası:")
    df.to_excel("ihtiyaç bulaşık.xlsx")
    st.write(df)




