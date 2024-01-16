import streamlit as st
import pickle


with open(r"model_uas.pkl", 'rb') as f:
    model = pickle.load(f)


features = ['age', 'sex', 'bmi', 'children', 'smoker',]


values = []
for feature in features:
    st.write(feature)
    value = st.number_input(feature)
    values.append(value)


if st.button('Submit'):
    prediction = model.predict([values])
    rounded_prediction = round(prediction[0])  # Memakai round() untuk membulatkan
    st.write('Prediksi biaya asuransi:', rounded_prediction)


st.write('NIM: 2020230018')
st.write('Nama: Muhammad Respati Abimanyu Putro')
