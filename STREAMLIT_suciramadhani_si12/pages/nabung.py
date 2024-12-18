import streamlit as st 

st.title("ini halaman Nabung!")

with st.form("nabung"):
    nama=st.text_input("masukan nama")
    nominal= st.number_input("masukan nominal nabung")
    submitButton = st.form_submit_button("save")

    if submitButton:
        st.write(nama)
        st.session_state["Nabung"].append({
            "nama":nama,
            "Nominal":nominal,
        })
        st.success("berhasil menabung!")