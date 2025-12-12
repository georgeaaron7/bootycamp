from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/multiply")
def multiply(a: int, b: int):
    return {"result": a * b}