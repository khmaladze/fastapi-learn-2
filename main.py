from typing import Optional
from fastapi import FastAPI,Path
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "name":"john",
        "age":17,
        "year":"Year 12"
    },
    2:{
        "name":"john 2",
        "age":18,
        "year":"Year 12"
    },
    3:{
        "name":"john 3",
        "age":19,
        "year":"Year 12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

@app.get('/hello')
def hello():
    return "hello world!"

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None,description="The ID of the student you want to view",gt=0,le=len(students))):
    return students[student_id]

# google.com/result?search=something

@app.get("/get-by-name/{student_id}")
def get_student(*,student_id: int, name: Optional[str] = None, test: int, age: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            if students[student_id]["age"] == age:
                return students[student_id]
    return {"Data":"Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error":"Student exists"}
    students[student_id] = student
    return students[student_id]