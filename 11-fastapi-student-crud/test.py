from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

#get -> read
# post -> create
# put -> update
# delete -> delete 
#patch -> to update selected field 
students = [
    {"id":1,"name":"Suresh"},
    {"id":2,"name":"Mahesh"},
    {"id":3,"name":"Ramesh"}
]

class Student(BaseModel):
    name:str

# to get home directory
@app.get("/")
def home():
    return "Hello from FastAPI"


#to get students details by passing parameter
@app.get("/students/{student_id}")

def get_student(student_id:int):
    for student in students:
        if student["id"]== student_id:
            return student
    return {"No student found"}

@app.put("/studentsupdate/{student_id}")
def update_student(student_id:int,data:Student):
    for student in students:
        if student["id"]== student_id:
            student["name"]==data.name
            return("Details updated successfully")
        
    return("Student not found")

@app.post("/studentsupdate")
def add_student(student_id:int,student: Student):
    new_student = {"id":id,"name":student.name}
    students.append(new_student)
    return {"students added sucessfully"}

@app.delete("/studentsdelete/{student_id}")
def delete_student(student_id:int):
    for student in students:
            if student["id"]== student_id:
                students.remove(student)
                return{"students deleted succesfully"}
    return{"No student found"}


  