import streamlit as st


def header_home():
   logo_url="https://i.ibb.co/YTYGn5qV/logo.png"
   st.markdown(f"""
        <div style='display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px;margin-top:30px;'>
        <img src='{logo_url}' style='height:100px;'/>
        </div>
        <h1 class="snap-title">
            SNAP</br>CLASS
        </h1>
        """,
        unsafe_allow_html=True
    )
def header_dashboard_teacher():
   logo_url="https://i.ibb.co/YTYGn5qV/logo.png"
   st.markdown(f"""
        <div style='display:flex; align-items:center; justify-content:flex-start; gap:10px; margin-top:20px'>
            <img src='{logo_url}' style='height:85px;'>
            <div>
                <h2 class="snap-teacher"style='text-align:left; color: #5865F2'>
                    SNAP</br>CLASS
                </h2>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )