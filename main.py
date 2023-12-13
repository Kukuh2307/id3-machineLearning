import pickle
import streamlit as st

# Model = '/home/kisawa16/Documents/KULIAH/MACHINE LEARNING/UTS/ID3/diabetes_decision_tree_model.pkl'
id3Model = pickle.load(open('diabetes_decision_tree_model.pkl', 'rb'))

st.title('Prediksi Penyakit diabetes')

col1,col2 = st.columns(2)

with col1:
    gender = st.text_input('Masukkan gender (female = 0, male = 1)')
    age = st.text_input('Masukkan umur')
    hypertension = st.text_input('Masukkan Hypertension')
    heart = st.text_input('Riwayat Jantung')

with col2:
    smoking = st.text_input('Masukkan smoking history (current = 3, never = 2, No info = 0, former = 1)')
    bmi = st.text_input('Masukkan BMI')
    hbaic = st.text_input('Masukkan HbAIc Level')
    blood = st.text_input('Masukkan Bloood glucose level')

if gender and age and hypertension and heart and smoking and bmi and hbaic and blood :
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