import streamlit as st
from src.screens.components.header_home import header_dashboard_teacher
from src.screens.ui.base_layout import style_base_dashboard,style_base_layout
from src.screens.components.footer_home import footer_dashboard
from src.screens.database.db import get_all_students,create_student,get_student_subjects,get_student_attendance,unenroll_student_to_subject
import numpy as np
from PIL import Image
from src.pipelines.face_pipeline import get_attendence,get_face_embeddings,train_classifier
from src.pipelines.voice_pipeline import get_voice_embeddings
from src.screens.components.dialog_enroll import enroll_dialog
from src.screens.components.subject_card import subject_card
def student_dashboard():
    student_data=st.session_state.student_data
    student_id=student_data['student_id']
    c1,c2=st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
        header_dashboard_teacher()
    with c2:
        st.subheader(f"""Welcome back {student_data['name']}""")
        if st.button("Logout",type='secondary',key="loginbackbtn",shortcut="ctrl+backspace"):
                st.session_state['is_logged_in']=False
                st.session_state.user_role = None
                if "student_data" in st.session_state:
                    del st.session_state.student_data
                st.rerun()
    st.space()
    c1,c2=st.columns(2)
    with c1:
        st.header("Your Enrolled Subjects")
    with c2:
        if st.button('Enroll in subject' ,type='primary',width='stretch'):
            enroll_dialog()

    st.divider()
    with st.spinner("Loading your enrolled subjects..."):
        subjects=get_student_subjects(student_id)
        logs=get_student_attendance(student_id)
    stats_map={}
    for log in logs:
        sid=log['subject_id']
        if sid not in stats_map:
            stats_map[sid]={'total':0,'attended':0}
        stats_map[sid]['total']+=1
        if log.get('is_present'):
            stats_map[sid]['attended']+=1


    cols=st.columns(2)
    for i,sub_node in enumerate(subjects):
        sub=sub_node['subjects']
        sid=sub['subject_id']

        stats=stats_map.get(sid,{'total':0,'attended':0})
        def unenroll_button():
                            if st.button("Unenroll from this course",type='tertiary',width='stretch',icon=":material/delete_forever:"):
                                
                                unenroll_student_to_subject(student_id,sid)
                                st.toast(f"Unenrolled from {sub['name']} successfully!")
                                st.rerun()
        with cols[i%2]:
            

            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=[
                    ("🗓️",'Total',stats['total']),
                    ("✅",'Attended',stats['attended'])
                ],
                footer_callback=unenroll_button()

            )



    footer_dashboard()




def students_screen():
    style_base_dashboard()
    style_base_layout()
    if "student_data" in st.session_state:
        student_dashboard()
        return
    c1,c2=st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
        header_dashboard_teacher()
    with c2:
        if st.button("go back to home",type='secondary',key="loginbackbtn",shortcut="ctrl+backspace"):
            st.session_state['login_state']=None
            st.rerun()
    st.header("Login using FaceId", text_alignment="center")
    st.space()
    st.space()
    show_registration=False
    photo_source=st.camera_input("Position your face in the center.")
    if photo_source:
        img=np.array(Image.open(photo_source))
        st.spinner("AI is scanning your face.")
        detected,all_ids,num_faces=get_attendence(img)
        if num_faces==0:
            st.warning("Face not found!")
        elif num_faces>1:
            st.warning("Multiple faces found!")
        else:
            if detected:
                student_id=list(detected.keys())[0]
                all_students=get_all_students()
                student=next((s for s in all_students if s['student_id']==student_id),None)

                if student:
                    st.session_state.is_logged_in=True
                    st.session_state.user_role="student"
                    st.session_state.student_data=student
                    st.toast(f"Welcome back {student['name']}")
                    import time
                    time.sleep(1)
                    st.rerun()
            else:
                st.info("Face not recognised! You might be a new student.")
                show_registration=True
    if show_registration==True:
        with st.container(border=True):
            st.header("Register your profile")
            new_name=st.text_input("Enter your name",placeholder="E.g sneha")
            st.subheader("Optional: Voice Enrollment")
            st.info("Enroll your voice for only attendance") 
            audio_data=None
            try:
                audio_data=st.audio_input("Record a short phrase like I am present .My name is Sneha.")
            except Exception:
                st.error("Audio input failed!")
            if st.button("Create Account ",type="primary"):
                if new_name:
                    with st.spinner("Creating Profile..."):
                        img=np.array(Image.open(photo_source))
                        encoding=get_face_embeddings(img)
                        if encoding:
                            face_embed=encoding[0].tolist()

                            voice_embed=None
                            if audio_data:
                                voice_embed=get_voice_embeddings(audio_data.read())

                            response_data=create_student(new_name,voice_embedding=voice_embed,face_embedding=face_embed)
                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in=True
                                st.session_state.user_role="student"
                                st.session_state.student_data=response_data[0]
                                st.toast(f"Profile Created,Hi {new_name}!")
                                import time
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error("Could'nt capture your facial feature for registration.")


                else:
                    st.warning("Please enter your name!")



    footer_dashboard()
    