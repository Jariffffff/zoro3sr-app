import streamlit as st
from auth import login
from ui import show_dashboard
from scraper import get_sample_data

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login()
else:
    st.sidebar.success("✅ Logged in")
    
    if 'data' not in st.session_state:
        st.session_state.data = get_sample_data()

    page = st.sidebar.radio("Navigate", ["📊 Dashboard", "🔍 Scraper", "⚙️ Settings"])
    
    if page == "📊 Dashboard":
        show_dashboard(st.session_state.data)
    elif page == "🔍 Scraper":
        st.info("🛠️ Scraper panel coming soon.")
    elif page == "⚙️ Settings":
        st.info("🔧 Settings panel coming soon.")