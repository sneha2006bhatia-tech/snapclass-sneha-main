import streamlit as st
import segno
import io

@st.dialog("Share Class Link")
def share_subject_dialog(subject_name,subject_code):
    st.markdown("""
        <style>
        /* Dialog background */
        [data-testid="stDialog"] [role="dialog"] {
            background-color: white !important;
            color: #1e293b !important;
        }

        /* Dialog headings and text */
        [data-testid="stDialog"] h1,
        [data-testid="stDialog"] h2,
        [data-testid="stDialog"] h3,
        [data-testid="stDialog"] p {
            color: #1e293b !important;
        }

        /* Code boxes */
        [data-testid="stDialog"] pre {
            background-color: #f1f5f9 !important;
            color: #1e293b !important;
        }
        </style>
    """, unsafe_allow_html=True)
    app_domain="snapclass-main-sneha.streamlit.app"
    join_url=f"{app_domain}/?join_code={subject_code}"

    st.header("Scan to join")
    qr=segno.make(join_url)
    out=io.BytesIO()
    qr.save(out,kind='png',scale=10,border=1)
    col1,col2=st.columns(2)
    with col1:
        st.markdown('### Copy Link')
        st.code(join_url,language="text")
        st.code(subject_code,language="text")
        st.info("Copy this link to share on Whatsapp or Email.")
    with col2:
        st.markdown("Scan to join")
        st.image(out.getvalue(),use_container_width=True,caption='QRCODE for class joining')