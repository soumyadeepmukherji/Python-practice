from fastapi import FastAPI, Path

app = FastAPI()

Students = {
    1: {
        "name":"Srikanth",
        "age": 19,
        "subject":"Physics"
        },

    2:{
        "name":"ganesh",
        "age": 17,
        "subject":"Biology"
    }
}

# GET Method
@app.get("/")
def index():
    return Students

#Path Parameters
@app.get("/get-students/{student_id}")
def get_student(student_id: int):
    return Students[student_id]