import streamlit as st
import pandas as pd


uploaded_file = st.file_uploader("Sipariş Dosyasını Yükleyin", type=["xlsx"])


if uploaded_file is not None:
    df = pd.read_excel(uploaded_file,sheet_name="bakiye")
    dfkanban = pd.read_excel(uploaded_file,sheet_name="kanban")
    dfsonirsaliye = pd.read_excel(uploaded_file,sheet_name="Sayfa3")
    dfdepobakiye = pd.read_excel(uploaded_file,sheet_name="depo")

    df = df[~df["KODU VE TANIMI"].str.contains("KPG")]

    ####################################  bakiye için kod birleştirme

    df.loc[df["MALZEME"] == 42187725, "MALZEME"] = 42303427
    df.loc[df["MALZEME"] == 42227001, "MALZEME"] = 42303427
    df.loc[df["MALZEME"] == 42246243, "MALZEME"] = 42303427
    df.loc[df["MALZEME"] == 42303425, "MALZEME"] = 42303427
    df.loc[df["MALZEME"] == 42303426, "MALZEME"] = 42303427

    df.loc[df["MALZEME"] == 42280324, "MALZEME"] = 42214622

    df.loc[df["MALZEME"] == 32052807, "MALZEME"] = 32012561
    df.loc[df["MALZEME"] == 32052806, "MALZEME"] = 32029268

    columns = df.columns
    columns = columns
    silinecek_sutunlar = ['MALZEME', 'KODU VE TANIMI']
    columns = [col for col in columns if col not in silinecek_sutunlar]
    df = df.groupby("MALZEME")[columns].sum()
    df.reset_index(inplace=True)

    ####################################  dfkanban için kod birleştirme

    dfkanban = pd.DataFrame(dfkanban)
    dfkanban.loc[dfkanban["KOD"] == 42187725, "KOD"] = 42303427
    dfkanban.loc[dfkanban["KOD"] == 42227001, "KOD"] = 42303427
    dfkanban.loc[dfkanban["KOD"] == 42246243, "KOD"] = 42303427
    dfkanban.loc[dfkanban["KOD"] == 42303425, "KOD"] = 42303427
    dfkanban.loc[dfkanban["KOD"] == 42303426, "KOD"] = 42303427

    dfkanban.loc[dfkanban["KOD"] == 42280324, "KOD"] = 42214622

    dfkanban.loc[dfkanban["KOD"] == 32052807, "KOD"] = 32012561
    dfkanban.loc[dfkanban["KOD"] == 32052806, "KOD"] = 32029268

    dfkanban = dfkanban.groupby("KOD").agg({"STOK": "sum"})
    dfkanban.reset_index(inplace=True)

    ####################################  depo bakiye için kod birleştirme
    dfdepobakiye = pd.DataFrame(dfdepobakiye)
    dfdepobakiye.loc[dfdepobakiye["STOK_KODU"] == 42187725, "STOK_KODU"] = 42303427
    dfdepobakiye.loc[dfdepobakiye["STOK_KODU"] == 42227001, "STOK_KODU"] = 42303427
    dfdepobakiye.loc[dfdepobakiye["STOK_KODU"] == 42246243, "STOK_KODU"] = 42303427
    dfdepobakiye.loc[dfdepobakiye["STOK_KODU"] == 42303425, "STOK_KODU"] = 42303427
    dfdepobakiye.loc[dfdepobakiye["STOK_KODU"] == 42303426, "STOK_KODU"] = 42303427

    dfdepobakiye.loc[dfdepobakiye["STOK_KODU"] == 42280324, "STOK_KODU"] = 42214622

    dfdepobakiye.loc[dfdepobakiye["STOK_KODU"] == 32052807, "STOK_KODU"] = 32012561
    dfdepobakiye.loc[dfdepobakiye["STOK_KODU"] == 32052806, "STOK_KODU"] = 32029268

    dfdepobakiye = dfdepobakiye.groupby("STOK_KODU").agg({"1 Nolu Depo": "sum"})
    dfdepobakiye.reset_index(inplace=True)

    ####################################  son irsaliye için kod birleştirme
    dfsonirsaliye = pd.DataFrame(dfsonirsaliye)
    dfsonirsaliye.loc[dfsonirsaliye["Stok Kodu"] == 42187725, "Stok Kodu"] = 42303427
    dfsonirsaliye.loc[dfsonirsaliye["Stok Kodu"] == 42227001, "Stok Kodu"] = 42303427
    dfsonirsaliye.loc[dfsonirsaliye["Stok Kodu"] == 42246243, "Stok Kodu"] = 42303427
    dfsonirsaliye.loc[dfsonirsaliye["Stok Kodu"] == 42303425, "Stok Kodu"] = 42303427
    dfsonirsaliye.loc[dfsonirsaliye["Stok Kodu"] == 42303426, "Stok Kodu"] = 42303427

    dfsonirsaliye.loc[dfsonirsaliye["Stok Kodu"] == 42280324, "Stok Kodu"] = 42214622

    dfsonirsaliye.loc[dfsonirsaliye["Stok Kodu"] == 32052807, "Stok Kodu"] = 32012561
    dfsonirsaliye.loc[dfsonirsaliye["Stok Kodu"] == 32052806, "Stok Kodu"] = 32029268

    dfsonirsaliye = dfsonirsaliye.groupby("Stok Kodu").agg({"Çıkış Miktarı": "sum"})
    dfsonirsaliye.reset_index(inplace=True)

    ####################################

    dfsonirsaliye = dfsonirsaliye[["Stok Kodu", "Çıkış Miktarı"]]
    dfsonirsaliye = dfsonirsaliye.groupby("Stok Kodu").agg({"Çıkış Miktarı": "sum"})

    dfdepobakiye = dfdepobakiye[["STOK_KODU", "1 Nolu Depo"]]
    dfdepobakiye = dfdepobakiye.rename(columns={"1 Nolu Depo": "Depo Bakiyesi"})

    dfkanban = dfkanban[["KOD", "STOK"]]
    dfkanban = dfkanban.rename(columns={"STOK": "Kanban"})
    df.fillna(0, inplace=True)
    df = pd.merge(df, dfkanban, how="left", left_on="MALZEME", right_on="KOD")
    df = pd.merge(df, dfsonirsaliye, how="left", left_on="MALZEME", right_on="Stok Kodu")
    df = pd.merge(df, dfdepobakiye, how="left", left_on="MALZEME", right_on="STOK_KODU")

    df = df.drop(columns=["STOK_KODU"])
    df_melted = pd.melt(df, id_vars=['MALZEME', "Kanban", "Depo Bakiyesi", "Çıkış Miktarı"]
                        , var_name='Tarih', value_name='Sipariş Miktarı')

    df = df_melted.sort_values(by=['MALZEME', 'Tarih'])

    df = df[df["Sipariş Miktarı"] != 0]
    df = df[df["MALZEME"] != "TOPL"]
    df = df[df["Tarih"] != "STOK_KODU"]
    df = df[df["Tarih"] != "Stok Kodu"]
    df = df[df["Tarih"] != "KOD"]

    df = df[df["MALZEME"] != 42199296]
    df = df[df["MALZEME"] != 42074682]
    df = df[df["MALZEME"] != 42290108]
    df = df[df["MALZEME"] != 42186714]

    df = df.dropna(subset=['Sipariş Miktarı'])
    df.fillna(0, inplace=True)

    df["Kanban"] = df["Kanban"] + df["Depo Bakiyesi"] + df["Çıkış Miktarı"]

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

    pivot_df = df.pivot_table(values='Sipariş Miktarı', index='MALZEME', columns='Tarih', aggfunc='sum', fill_value=0)

    df.to_excel("ihtiyaç bulaşık.xlsx")
    st.write(pivot_df)
    st.write(df)



