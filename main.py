import streamlit as st

st.title("System Module Import Test")

try:
    import sys
    st.success("Imported sys module successfully!")
    st.write(f"Python version: {sys.version}")
    st.write(f"sys.path: {sys.path}")
except Exception as e:
    st.error(f"Failed to import sys module: {e}")

st.write("Add your app logic below this.")



