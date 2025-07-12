import streamlit as st
import plotly.express as px
from datetime import datetime

def show_dashboard(data):
    st.markdown("""
        <style>
            body { background-color: #0F0F0F; color: white; }
            .metric-box {
                background: #1A1A1A;
                padding: 1.5rem;
                border-radius: 1rem;
                box-shadow: 0 2px 6px rgba(0,0,0,0.3);
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("## 🧠 Product Overview")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"<div class='metric-box'><h4>Total</h4><p>{len(data)}</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='metric-box'><h4>Avg Price</h4><p>৳{round(data['price'].mean(), 2)}</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='metric-box'><h4>Top Cat</h4><p>{data['category'].mode()[0]}</p></div>", unsafe_allow_html=True)
    with col4:
        st.markdown(f"<div class='metric-box'><h4>Synced</h4><p>{datetime.now().strftime('%b %d')}</p></div>", unsafe_allow_html=True)

    st.markdown("### 🔎 Filters")
    col1, col2 = st.columns(2)
    with col1:
        selected = st.selectbox("Select Category", ["All"] + list(data['category'].unique()))
    with col2:
        search = st.text_input("Search Title")

    filtered = data.copy()
    if selected != "All":
        filtered = filtered[filtered['category'] == selected]
    if search:
        filtered = filtered[filtered['title'].str.contains(search, case=False)]

    st.markdown("### 📊 Category Price Chart")
    fig = px.bar(
        filtered.groupby("category")["price"].mean().reset_index(),
        x="category", y="price", color="category",
        title="Avg Price by Category", template="plotly_dark"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📋 Data Table")
    st.dataframe(filtered, use_container_width=True)

    csv = filtered.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download CSV", csv, "filtered_zoro3sr.csv", "text/csv")