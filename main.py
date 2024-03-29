from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "name":"person 1",
        "age": 17,
        "year":"Year 12"
    },
    2:{
        "name":"person 2",
        "age": 18,
        "year":"Year 12"
    },
    3:{
        "name":"person 3",
        "age": 19,
        "year":"Year 12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get('/hello')
def hello():
    return "hello world!"

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None,description="The ID of the student you want to view",gt=0)):
    for student_id in students:    
        return students[student_id]
    return {"Data":"Not Found"}

# @app.get("/get-by-name/{student_id}")
# def get_student(*,student_id: int, name: Optional[str] = None, test: int, age: int):
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             if students[student_id]["age"] == age:
#                 return students[student_id]
#     return {"Data":"Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error":"Student exists"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error":"Student does not exist"}

    if student.name != None:
        students[student_id]["name"] = student.name

    if student.age != None:
        students[student_id]["age"] = student.age
    
    if student.year != None:
        students[student_id]["year"] = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error":"Student Does Not Exists"}
    
    del students[student_id]
    return {"Message":"User Deleted SuccessFully"}