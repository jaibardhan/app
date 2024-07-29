from fastapi import FastAPI, HTTPException
from fastapi import status
#Initializes the FastAPI application.
app = FastAPI()

#http://127.0.0.1:8000/
@app.get("/", status_code=status.HTTP_200_OK)
def welcome():
    return {"msg": "This is home page of FastAPI main module."}


#http://127.0.0.1:8000/JaiBardhan
@app.get("/{name}", status_code=status.HTTP_200_OK)
def welcome(name):
    return {"msg": f"Welcome to FastAPI Mr.{name}"}
