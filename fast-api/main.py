from fastapi import FastAPI,HTTPException
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Welcome you all !"}
@app.get("/greet/{name}")
def greet(name):
    return {"message": f"Hello, {name}!"}
@app.get("/multiply")
def multiply(a:int,b:int):
    return{"ANS":a*b}
Studentslist={"Aiden":"001","Bella":"002","Catherine":"003","David":"004"}
@app.get("/students")
def students():
    return Studentslist
@app.get("/students/{name}")
def find_student(name):
    if name not in Studentslist:
        raise HTTPException
    return f'{name}:{Studentslist[name]}'
@app.post("/students/{name}")
def add_student(name,id):
    Studentslist[name] = id     
    return Studentslist
@app.put("/students/{name}")
def update_data(name:str,id:int):
    if name not in Studentslist:
        raise HTTPException
    Studentslist[name] = id
    return {"updated list":Studentslist}
@app.delete("/students/{name}")
def del_data(name):
    if name not in Studentslist:
        raise HTTPException(status_code=404)
    del Studentslist[name]
    return Studentslist
