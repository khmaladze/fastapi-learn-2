from fastapi import FastAPI,Path

app = FastAPI()

students = {
    1:{
        "name":"john",
        "age":17,
        "class":"Year 12"
    },
    2:{
        "name":"john 2",
        "age":17,
        "class":"Year 12"
    },
    3:{
        "name":"john 3",
        "age":17,
        "class":"Year 12"
    }
}

@app.get('/hello')
def hello():
    return "hello world!"

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None,description="The ID of the student you want to view",gt=0,le=len(students))):
    return students[student_id]

# google.com/result?search=something