import streamlit as st
from src.screens.database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of new subject.")
    subject_name=st.text_input("Enter Subject Name",placeholder="Introduction to Computer Science.")
    subject_id=st.text_input("Enter Subject Code",placeholder="NCS101")
    subject_section=st.text_input("Enter Your Section",placeholder="A")

    if st.button("Create New Subject",width="stretch",type="primary"):
        if subject_id and subject_name and subject_section:
            try:
                create_subject(subject_id,subject_name,subject_section,teacher_id)
                st.toast("Subject Created Successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please fill all the fields!")

