from src.screens.database.config import supabase
import bcrypt

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(),bcrypt.gensalt()).decode()



def check_teacher_exist(username):
    response=supabase.table("teachers").select("username").eq("username",username).execute()
    return len(response.data)>0
def check_pass(pwd,hashed):
    return bcrypt.checkpw(pwd.encode(),hashed.encode())

def create_teacher(username,password,name):
    data={"username":username,"password":hash_pass(password),"name":name}
    response=supabase.table("teachers").insert(data).execute()
    return response.data

def login_teacher(username,password):
    response=supabase.table("teachers").select("*").eq("username",username).execute()
    if response.data:
        teacher=response.data[0]
        if check_pass(password,teacher['password']):
            return teacher
    return None

def get_all_students():
    response=supabase.table("students").select("*").execute()
    return response.data
def create_student(new_name,face_embedding=None,voice_embedding=None):
    data={'name':new_name,'face_embedding':face_embedding,'voice_embedding':voice_embedding}
    response=supabase.table("students").insert(data).execute()
    return response.data
def create_subject(subject_code,name,section,teacher_id):
    data={'subject_code':subject_code,'name':name,'section':section,'teacher_id':teacher_id}
    response=supabase.table("subjects").insert(data).execute()
    return response.data
def get_teacher_subjects(teacher_id):
   
    response = (
        supabase
        .table("subjects")
        .select("*")
        .eq("teacher_id", teacher_id)
        .execute()
    )

    subjects = response.data

    for sub in subjects:
        subject_id = sub["subject_id"]

        # Count students enrolled in this subject
        student_response = (
            supabase
            .table("subject_students")
            .select("student_id")
            .eq("subject_id", subject_id)
            .execute()
        )

        sub["total_students"] = len(student_response.data)

        # Get attendance timestamps for this subject
        attendance_response = (
            supabase
            .table("attendance_logs")
            .select("timestamp")
            .eq("subject_id", subject_id)
            .execute()
        )

        timestamps = [
            log["timestamp"]
            for log in attendance_response.data
            if log.get("timestamp")
        ]

        # Number of unique attendance sessions/classes
        sub["total_classes"] = len(set(timestamps))

    return subjects



def enroll_student_to_subject(student_id,subject_id):
    data={'student_id':student_id,'subject_id':subject_id}
    response=supabase.table('subject_students').insert(data).execute()
    return response.data

def unenroll_student_to_subject(student_id,subject_id):
    
    response=supabase.table('subject_students').delete().eq('student_id',student_id).eq('subject_id',subject_id).execute()
    return response.data
def get_student_subjects(student_id):
    response=supabase.table('subject_students').select('*','subjects(*)').eq('student_id',student_id).execute()
    return response.data
def get_student_attendance(student_id):
    response=supabase.table('attendance_logs').select('*','subjects(*)').eq('student_id',student_id).execute()
    return response.data
def create_attendance(logs):
    response=supabase.table('attendance_logs').insert(logs).execute()
    return response.data
def get_attendance_for_teacher(teacher_id):
    response=supabase.table('attendance_logs').select("*,subjects!inner(*)").eq("subjects.teacher_id",teacher_id).execute()
    return response.data
