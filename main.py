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
        if not st.session_state.authenticated:
    login()
else:
    st.sidebar.success(f"✅ Logged in as {st.session_state.username} ({st.session_state.role})")

    if 'data' not in st.session_state:
        st.session_state.data = get_sample_data()

    page = st.sidebar.radio("Navigate", ["📊 Dashboard", "🔍 Scraper", "⚙️ Settings"])

    if page == "📊 Dashboard":
        show_dashboard(st.session_state.data)
    elif page == "🔍 Scraper":
        if st.session_state.role == "admin":
            st.info("🛠️ Scraper panel (admin only)")
        else:
            st.warning("⚠️ Only admin can access scraper.")
    elif page == "⚙️ Settings":
        st.info("🔧 Settings panel coming soon.")
