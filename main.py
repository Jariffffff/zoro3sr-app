import streamlit as st
from scraper import scrape_all  # Ensure scraper.py is in your project root

st.title("Zoro3sr Multi-Source Product Scraper")

# User inputs
query = st.text_input("Enter search query", value="headphones")
source = st.selectbox("Select e-commerce source", options=["daraz", "pickaboo", "rokomari"])
pages = st.number_input("Number of pages to scrape", min_value=1, max_value=5, value=1)

if st.button("Scrape"):
    with st.spinner(f"Scraping {pages} page(s) from {source}..."):
        try:
            df = scrape_all(query, source, pages)
            if df.empty:
                st.warning("No results found.")
            else:
                st.success(f"Found {len(df)} items.")
                st.dataframe(df)
        except Exception as e:
            st.error(f"Error during scraping: {e}")


