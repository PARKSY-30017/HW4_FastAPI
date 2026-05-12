from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()


class Course(BaseModel):
    course_name: str
    year: str
    semester: str
    grade: str


@app.get("/courses")
def get_courses():

    with open("courses.json", "r", encoding="utf-8") as file:
        courses = json.load(file)

    return courses


@app.post("/courses")
def add_course(course: Course):

    with open("courses.json", "r", encoding="utf-8") as file:
        courses = json.load(file)

    courses.append(course.dict())

    with open("courses.json", "w", encoding="utf-8") as file:
        json.dump(courses, file, ensure_ascii=False, indent=2)

    return {
        "message": "Course added successfully",
        "course": course
    }