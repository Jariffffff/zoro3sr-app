import streamlit as st
import os
import sys

# Debug: show environment info
st.write("📁 Current working directory:", os.getcwd())
st.write("🐍 Python sys.path:", sys.path)

# Optional: force scraper path (in case import still fails)
sys.path.append("./scraper")

# --- Main Imports ---
from auth import login
from base import scrape_all  # using base directly after sys.path.append
from ui import show_dashboard
# from google_export import export_to_gsheet  # Optional

# --- Session state defaults ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login()
else:
    st.sidebar.success(f"✅ Logged in as {st.session_state.username} ({st.session_state.role})")

    # --- Scraper UI ---
    st.sidebar.markdown("## 🔍 Product Scraper")
    source = st.sidebar.selectbox("🛒 E-commerce Site", ["daraz", "pickaboo", "rokomari"])
    query = st.sidebar.text_input("Search Term", value="headphones")
    pages = st.sidebar.slider("Pages to Scrape", 1, 3, 1)

    if st.sidebar.button("🔄 Scrape"):
        with st.spinner("Scraping data live..."):
            st.session_state.data = scrape_all(query=query, source=source, pages=pages)
            st.success(f"✅ Scraped from {source.title()}")

    # --- Default scrape fallback ---
    if 'data' not in st.session_state:
        st.session_state.data = scrape_all(query="headphones", source="daraz", pages=1)

    # --- Navigation ---
    page = st.sidebar.radio("Navigate", ["📊 Dashboard", "🔍 Raw Data", "⚙️ Settings"])

    # --- Page logic ---
    if page == "📊 Dashboard":
        show_dashboard(st.session_state.data)

    elif page == "🔍 Raw Data":
        st.subheader(f"🛍 Products from {source.title()}")
        st.dataframe(st.session_state.data)

        # Export buttons
        st.download_button("⬇️ Download CSV", st.session_state.data.to_csv(index=False), "products.csv", "text/csv")

        # Optional GSheet
        # if st.button("📤 Export to Google Sheets"):
        #     export_to_gsheet(st.session_state.data, "Zoro3srExport")
        #     st.success("✅ Exported to Google Sheets")

    elif page == "⚙️ Settings":
        st.info("More configuration options will be added soon.")


