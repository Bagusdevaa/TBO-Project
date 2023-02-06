import process, general
import streamlit as st

st.title("APLIKASI PENGECEKAN TATA BAHASA INDONESIA")
st.write("Aplikasi ini adalah untuk mengecek tata bahasa dari bahasa Indonesia")

kalimat = st.text_input("Masukkan kalimat yang akan dicek")
button = st.button("Check")

if button:
    if general.check_alphabet(kalimat.lower().split()) == False:
        st.error("Kalimat Tidak Valid Karena Terdapat Kata Yang Belum Ada Di Data File")
    elif process.table_filling_process(kalimat.lower().split()) == True:
        st.success("Kalimat Diterima Karena Sesuai Dengan Pola Dan Persyaratan")
    else:
        st.error("Kalimat Ditolak Karena Tidak Sesuai Dengan Pola Dan Persyaratan")
