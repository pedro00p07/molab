import streamlit as st

tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

with tab1:
    st.radio("Select one:", [1, 2])
