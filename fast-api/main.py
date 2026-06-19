from fastapi import FastAPI
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
