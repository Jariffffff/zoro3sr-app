import streamlit as st
import json

def load_users():
    with open("users.json", "r") as f:
        return json.load(f)

def login():
    st.title("🔐 Zoro3sr Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")

    if login_btn:
        users = load_users()
        user = users.get(username)
        if user and user["password"] == password:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.role = user["role"]
            st.success(f"✅ Welcome {username} ({user['role']})")
            st.rerun()
        else:
            st.error("❌ Invalid credentials")
