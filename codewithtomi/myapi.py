from fastapi import FastAPI, Path
from typing import Optional
#create app
app = FastAPI()

students = {
    1: {
        "name":"john",
        "age":17,
        "class":"year 12"
    }
}

#create endpoint
@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int=Path(description="Enter student id")):
    return students[student_id]


@app.get("/get-by-name/{student_id}")
# def get_by_name(name: str=None):
def get_by_name(*,student_id:int, name:Optional[str]=None, test:int=None):
    # print(test)
    print(student_id)
    if(student_id in students):
        return students[student_id]
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"data":"not found"}

