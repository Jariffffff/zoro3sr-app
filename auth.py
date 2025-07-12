import streamlit as st

def login():
    st.title("🔐 Zoro3sr Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")

    if login_btn:
        if username == "admin" and password == "zoro123":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ Invalid credentials")