import streamlit as st
import mymodel as m

st.write("""
# Weekdays vs Weekend
This is the difference on weekdays vs weekends in 2022.         
""")
st.write(m.run(window=15))