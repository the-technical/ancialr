from fastapi import FastAPI, HTTPException
import uuid
import re

app = FastAPI()

students = {}
courses = {}
enrollments = {}

def is_valid_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

@app.post("/students")
def create_student(name: str, email: str):
    if not is_valid_email(email):
        raise HTTPException(status_code=400, detail="Invalid email format")
    student_id = str(uuid.uuid4())
    student = {"id": student_id, "name": name, "email": email}
    students[student_id] = student
    enrollments[student_id] = set()
    return student

@app.post("/courses")
def create_course(title: str, capacity: int):
    if capacity <= 0:
        raise HTTPException(status_code=400, detail="Capacity must be positive")
    course_id = str(uuid.uuid4())
    course = {"id": course_id, "title": title, "capacity": capacity, "enrolledCount": 0}
    courses[course_id] = course
    return course

@app.post("/enroll")
def enroll_student(student_id: str, course_id: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    if course_id not in courses:
        raise HTTPException(status_code=404, detail="Course not found")
    course = courses[course_id]
    if course["enrolledCount"] >= course["capacity"]:
        raise HTTPException(status_code=400, detail="Course is full")
    if course_id in enrollments[student_id]:
        raise HTTPException(status_code=400, detail="Student already enrolled")
    enrollments[student_id].add(course_id)
    course["enrolledCount"] += 1
    return {"message": f"Student enrolled in {course['title']}"}

@app.get("/students/{student_id}/courses")
def get_student_courses(student_id: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    course_ids = enrollments[student_id]
    return [courses[cid] for cid in course_ids]

@app.get("/courses/{course_id}/students")
def get_course_students(course_id: str):
    if course_id not in courses:
        raise HTTPException(status_code=404, detail="Course not found")
    student_list = [students[sid] for sid, cids in enrollments.items() if course_id in cids]
    return student_list

@app.delete("/unenroll")
def unenroll_student(student_id: str, course_id: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    if course_id not in courses:
        raise HTTPException(status_code=404, detail="Course not found")
    if course_id not in enrollments[student_id]:
        raise HTTPException(status_code=400, detail="Student not enrolled in this course")
    enrollments[student_id].remove(course_id)
    courses[course_id]["enrolledCount"] -= 1
    return {"message": "Unenrolled successfully"}
