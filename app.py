import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.teachers_screen import teacher_screen
from src.screens.students_screen import students_screen
from src.screens.components.dialog_auto_enroll import auto_enroll_dialog
def main():
    st.set_page_config("Snap Class-Making Attnedance faster using AI.",
                       page_icon="https://i.ibb.co/YTYGn5qV/logo.png"
                       )
    if 'login_state' not in st.session_state:
        st.session_state['login_state'] = None
    match st.session_state['login_state']:
        case "teacher":
            teacher_screen()
        case "student":
            students_screen()
        case None:
            home_screen()

    join_code=st.query_params.get('join_code')
    if join_code:
        if st.session_state.get('login_type') != 'student':
            st.session_state['login_type'] = 'student'
            st.session_state['login_state'] = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role')=='student':
            auto_enroll_dialog(join_code)
            st.rerun()
main()