import pickle
import streamlit as st

id3Model = pickle.load(open('diabetes_decision_tree_model.pkl', 'rb'))

st.title('ID3 - Prediksi Penyakit diabetes')

col1,col2 = st.columns(2)

with col1:
        gender = st.selectbox(
            "Pilih Jenis kelamin",
            ['Female','Male'],
            index=0
        )
        age = st.text_input('Masukkan umur')
        hypertension = st.text_input('Masukkan Hypertension')
        heart = st.text_input('Riwayat Jantung')

with col2:
        smoking = st.selectbox(
            "Masukkan smoking history",
            ['current','never','no info','former'],
            index=0
        )
        bmi = st.text_input('Masukkan BMI')
        hbaic = st.text_input('Masukkan HbAIc Level')
        blood = st.text_input('Masukkan Bloood glucose level')

if gender and age and hypertension and heart and smoking and bmi and hbaic and blood :

        gender = 0 if gender == "Female" else 1 

        smoking_mapping = {'current': 3, 'never': 2, 'no info': 0, 'former': 1}
        smoking = smoking_mapping[smoking]

        if smoking == 'current':
            smoking = 3
        if smoking == 'never':
            smoking = 2
        if smoking == 'no info':
            smoking = 0
        if smoking == 'former':
            smoking = 1
        input_data = [
            float(gender),float(age),float(hypertension),float(heart),float(smoking),float(bmi),float(hbaic),float(blood)]

        diabetes_diagnosis = ''

        if st.button('Test Prediksi Penyakit Diabetes'):
            diabetes_predict = id3Model.predict([input_data])

            if diabetes_predict[0] == 1:
                diabetes_diagnosis = 'Pasien terindikasi terkena penyakit diabetes'
            else:
                diabetes_diagnosis = 'Pasien terindikasi tidak terkena penyakit diabetes'

        st.success(diabetes_diagnosis)
else:
        st.warning('Masukkan semua nilai atribut sebelum melakukan prediksi')