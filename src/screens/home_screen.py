import streamlit as st
from src.screens.components.footer_home import footer_home
from src.screens.components.header_home import header_home
from src.screens.ui.base_layout import style_base_home, style_base_layout
def home_screen():
    
    

    style_base_home()
    style_base_layout()
    header_home()
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.header("I am a teacher")
        st.image(r"C:\Users\ranas\OneDrive\Desktop\snapclass\src\screens\assests\teacher.png",width=145)
        if st.button("teacher portal",key="teacher",icon=":material/arrow_outward:",icon_position="right"):
            st.session_state['login_state']="teacher"
            st.rerun()
    with col2:
        st.header("I am a student")
        st.image(r"C:\Users\ranas\OneDrive\Desktop\snapclass\src\screens\assests\student.png",width=160)
        if st.button("student portal",key="student",icon=":material/arrow_outward:",icon_position="right"):
            st.session_state['login_state']="student"
            st.rerun()
    footer_home()
