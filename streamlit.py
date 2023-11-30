import streamlit as st


excel_path = r'makine saat-eylül-ekim.xlsx'

# Excel dosyasını okuma
df = pd.read_excel(excel_path)
st.dataframe(df.head(5))

st.button('Hit me')

st.checkbox('Check me out')
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')


st.color_picker('Pick a color')


