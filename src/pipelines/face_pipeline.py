import dlib
import face_recognition_models
import numpy as np
from sklearn.svm import SVC
import streamlit as st
from src.screens.database.db import get_all_students


@st.cache_resource
def load_dlib_models():

    detector=dlib.get_frontal_face_detector()


    sp=dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec=dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )
    return detector,sp,facerec

def get_face_embeddings(Image_np):
    detector,sp,facerec=load_dlib_models()
    faces=detector(Image_np,1)
    Encodings=[]
    for face in faces:
        shape=sp(Image_np,face)
        face_descriptor=facerec.compute_face_descriptor(Image_np,shape,1)#128 embedding is generated

        Encodings.append(np.array(face_descriptor))
    return Encodings
@st.cache_resource
def get_trained_model():
    X=[]
    y=[]

    student_db=get_all_students()
    if not student_db:
        return None
    for student in student_db:
        embedding=student.get('face_embedding')
        if embedding:
            X.append(np.array(embedding))
            y.append(student.get('student_id'))
    if len(X)==0:
        return 0

    clf=SVC(kernel="linear",probability=True,class_weight="balanced")

    try:
        clf.fit(X,y)
    except ValueError:
        pass
    return{"clf":clf,"X":X,"y":y}

def train_classifier():
    st.cache_resource.clear()
    model_data=get_trained_model()
    return bool(model_data)



def get_attendence(class_image_np):

    encodings = get_face_embeddings(class_image_np)

    detected_students = {}

    student_db = get_all_students()

    if not student_db:
        return detected_students, [], len(encodings)

    # Get students who have face embeddings
    students_with_faces = []

    for student in student_db:

        embedding = student.get("face_embedding")

        if embedding:

            students_with_faces.append({
                "student_id": student.get("student_id"),
                "embedding": np.array(embedding)
            })

    if not students_with_faces:
        return detected_students, [], len(encodings)

    all_students = [
        student["student_id"]
        for student in students_with_faces
    ]

    # Check every detected face
    for encoding in encodings:

        best_student_id = None
        best_distance = float("inf")

        # Compare current face with every registered student
        for student in students_with_faces:

            stored_embedding = student["embedding"]

            distance = np.linalg.norm(
                stored_embedding - encoding
            )

            if distance < best_distance:

                best_distance = distance
                best_student_id = student["student_id"]

        # Recognition threshold
        recognition_threshold = 0.55

        if (
            best_student_id is not None
            and best_distance <= recognition_threshold
        ):

            detected_students[best_student_id] = True

    return (
        detected_students,
        all_students,
        len(encodings)
    )

