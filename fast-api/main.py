from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()
class Student(BaseModel):
    id: int
Studentslist={"Aiden":"001","Bella":"002","Catherine":"003","David":"004"}
@app.get("/students")
def students():
    return Studentslist
@app.get("/students/{name}")
def find_student(name:str):
    if name not in Studentslist:
        raise HTTPException
    return f'{name}:{Studentslist[name]}'
@app.post("/students/{name}")
def add_student(name:str,id:int):
    Studentslist[name] = id     
    return Studentslist
@app.put("/students/{name}")
def update_data(name:str,id:int):
    if name not in Studentslist:
        raise HTTPException(status_code=422)
    Studentslist[name] = id
    return {"updated list":Studentslist}
@app.delete("/students/{name}")
def del_data(name:str):
    if name not in Studentslist:
        raise HTTPException(status_code=404)
    del Studentslist[name]
    return Studentslist
