import streamlit as st

def style_base_home():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #5865F2 !important;
        }
         /* Cards */
        [data-testid="stColumn"] {
            background-color: #E0E3FF !important;
            border-radius: 2.5rem !important;

            padding: 1rem !important;

            height: 270px !important;

            text-align: center !important;
            box-sizing: border-box !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
        }

        /* Heading inside cards */
        [data-testid="stColumn"] h2,
        [data-testid="stColumn"] h1 {
            margin-top: 0 !important;
            margin-bottom: 0.5rem !important;
            text-align: center !important;
        }
        /* Keep the page centered */
        .block-container {
            max-width: 750px !important;
            margin: auto !important;
            padding-top: 1rem !important;
                }
            
        /* Center images */
        [data-testid="stColumn"] img {
            display: block !important;
            margin: 20px auto !important;
        }

        /* Center buttons inside cards */
        [data-testid="stColumn"] [data-testid="stButton"] {
           
            display: flex !important;
            justify-content: center !important;
            width: 100% !important;
            margin-top: 0 !important;
            position: relative !important;
            top: -35px !important;
        }

        /* Fix button size */
        [data-testid="stColumn"] [data-testid="stButton"] > button {
            width: 160px !important;
            min-width: 160px !important;
            height: 50px !important;

            white-space: nowrap !important;
            

            
        }
        </style>
        """,
        unsafe_allow_html=True
    )
        


def style_base_dashboard():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #E0E3FF !important;
        }
         /* =========================
           TEXT INPUTS
           ========================= */

        [data-testid="stTextInput"] div[data-baseweb="input"] {
            background-color: white !important;
            border: 1px solid #999999 !important;
            border-radius: 10px !important;
            box-shadow: none !important;
        }

        [data-testid="stTextInput"] div[data-baseweb="base-input"] {
            background-color: white !important;
        }

        [data-testid="stTextInput"] input {
            background-color: white !important;
            color: black !important;
            -webkit-text-fill-color: black !important;
            border: none !important;
            box-shadow: none !important;
        }

        [data-testid="stTextInput"] input::placeholder {
            color: #777777 !important;
            -webkit-text-fill-color: #777777 !important;
            opacity: 1 !important;
        }

        /* Input labels */
        [data-testid="stTextInput"] label {
            color: black !important;
        }


        /* =========================
           PASSWORD EYE BUTTON
           ========================= */

        [data-testid="stTextInput"] button {
            background-color: #5865F2 !important;
            color: white !important;

            border: none !important;
            border-radius: 0 9px 9px 0 !important;

            padding: 0 !important;
            margin: -1px -1px -1px 0 !important;

            height: calc(100% + 2px) !important;
            width: 70px !important;
            min-width: 70px !important;

            display: flex !important;
            align-items: center !important;
            justify-content: center !important;

            transform: none !important;
        }

        [data-testid="stTextInput"] button:hover {
            background-color: #5865F2 !important;
            transform: none !important;
        }

        [data-testid="stTextInput"] button:focus {
            background-color: #5865F2 !important;
            box-shadow: none !important;
        }

        /* =========================
           DIVIDER
           ========================= */

        hr {
            border: none !important;
            border-top: 2px solid #B8B8B8 !important;
            margin-top: 25px !important;
            margin-bottom: 25px !important;
        }

        </style>
    """,
    unsafe_allow_html=True
    )
def style_base_layout():
    st.markdown(
        """
        
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979..2050&family=Outfit:wght@100..900&display=swap');
        /*hide top bar of streamlit*/
        #MainMenu,header,footer,
        [data-testid="stHeader"],
        [data-testid="stToolbar"]{
        display: none !important;
        }
        .block-container{
        padding-top:1rem !important;}
        .snap-title {
        font-family: "Climate Crisis", sans-serif !important;
        font-variation-settings: "YEAR" 1979 !important;
        font-size: 3.5rem !important;
        font-weight: 400 !important;
        line-height: 0.9 !important;
        text-align: center !important;
        margin: 0 !important;
        color:white !important;
        }
        .snap-teacher {
            margin: 0 !important;
            padding: 0 !important;
            color: #5865F2 !important;
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 32px !important;
            line-height: 0.85 !important;
            text-align: left;
        }
        h1{
            font-family: "Climate Crisis", sans-serif !important;
            font-variation-settings: "YEAR" 1979 !important;
            font-size: 1.6rem !important;
            font-weight: 400 !important;
            line-height: 0.9 !important;
            text-align: center !important;
            margin: 0 !important;
            color: black !important;
            }  
        h2{
            font-family: "Climate Crisis", sans-serif !important;
            font-variation-settings: "YEAR" 1979 !important;
            font-size: 1.6rem !important;
            font-weight: 400 !important;
            line-height: 0.9 !important;
            text-align: center !important;
            margin: 0 !important;
            color: black !important;
            }
        h3{
        font-family: "Outfit", sans-serif !important;
        color:black !important;
        }    
        h4,p{
        font-family: "Outfit", sans-serif !important;
        
        }
        button{
            border-radius:1.5rem !important;
            background-color: #5865F2 !important;
            color:white !important;
            padding:10px 20px !important;
            border:none !important;
            transition: transform 0.25s ease !important;
        }
        button[kind="secondary"]{
        border-radius:1.5rem !important;
        background-color: #EB459E !important;
        color:white !important;
        padding:10px 20px !important;
        border:none !important;
        transition: transform 0.25s ease !important;
        }
        button[kind="tertiary"]{
            border-radius:1.5rem !important;
            background-color: black !important;
            color:white !important;
            padding:10px 20px !important;
            border:none !important;
            transition: transform 0.25s ease !important;
        }
        button:hover{
            transform: scale(1.05) !important;
        }
        /* =========================
        STREAMLIT DIALOG
        ========================= */

        [data-testid="stDialog"] > div {
            background-color: #ffffff !important;
        }

        [data-testid="stDialog"] [role="dialog"] {
            background-color: #ffffff !important;
            color: #000000 !important;
        }

        /* Dialog headings */
        [data-testid="stDialog"] h1,
        [data-testid="stDialog"] h2,
        [data-testid="stDialog"] h3 {
            color: #000000 !important;
        }

        /* Dialog normal text */
        [data-testid="stDialog"] p,
        [data-testid="stDialog"] label {
            color: #000000 !important;
        }

        /* Dialog buttons */
        [data-testid="stDialog"] button {
            color: white !important;
        }
        /* =================================
        GLOBAL STREAMLIT DIALOG STYLE
        ================================= */

        [data-testid="stDialog"] {
            color-scheme: light !important;
        }

        [data-testid="stDialog"] > div[role="dialog"] {
            background-color: #ffffff !important;
            color: #000000 !important;
        }

        [data-testid="stDialog"] > div[role="dialog"] > div {
            background-color: #ffffff !important;
            color: #000000 !important;
        }

        /* Dialog content */
        [data-testid="stDialog"] [data-testid="stDialogContent"] {
            background-color: #ffffff !important;
            color: #000000 !important;
        }

        /* All headings inside dialogs */
        [data-testid="stDialog"] h1,
        [data-testid="stDialog"] h2,
        [data-testid="stDialog"] h3,
        [data-testid="stDialog"] h4 {
            color: #000000 !important;
        }

        /* Normal text */
        [data-testid="stDialog"] p,
        [data-testid="stDialog"] label,
        [data-testid="stDialog"] span {
            color: #000000;
        }

        /* Don't make buttons white */
        [data-testid="stDialog"] button {
            color: white !important;
        }

        </style>
    """,
    unsafe_allow_html=True
    )