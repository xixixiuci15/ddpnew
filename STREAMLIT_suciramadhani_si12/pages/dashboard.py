import streamlit as st 

st.title("ini halaman dashboard!")
st.session_state["Nabung"]

jumlah=0
for session in st.session_state ["Nabung"]:
    jumlah += session ["Nominal"]

st.write("total nominal menabung anda sebesar", jumlah)

