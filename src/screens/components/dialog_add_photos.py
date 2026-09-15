import streamlit as st
from src.screens.database.db import enroll_student_to_subject
from src.screens.database.config import supabase
from PIL import Image
@st.dialog("Capture or Upload Photos")
def add_photos_dialog():

    st.write("Add classroom photos to scan for attendance.")

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab='camera'
    t1,t2=st.columns(2)

    with t1:
        type_camera='primary' if st.session_state.photo_tab=='camera' else 'secondary'
        if st.button('Camera',type=type_camera,width='stretch'):
            st.session_state.photo_tab='camera'

    with t2:
        type_upload='primary' if st.session_state.photo_tab=='upload' else 'secondary'
        if st.button('Upload photos',type=type_upload,width='stretch'):
            st.session_state.photo_tab='upload'

    if st.session_state.photo_tab=='camera':
        cam_photos=st.camera_input("Take Snapshot",key='dialog_cam')
        if cam_photos:
            st.session_state.attendance_images.append(Image.open(cam_photos))
            st.toast("Photo Captured")
            st.rerun()
    if st.session_state.photo_tab=='upload':
        upload_files=st.file_uploader( 'choose image files',type= ['png','jpg','jpeg'],accept_multiple_files=True,key='dialog_upload')
        if upload_files:
            for f in upload_files:
                st.session_state.attendance_images.append(Image.open(f))
            st.toast("Photos Uploaded Successfully")
            st.rerun()
        st.divider()
        if st.button('Done',type='primary',width='stretch'):
            
            st.rerun()
