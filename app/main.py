from ast import Return
from pdb import post_mortem
from random import randrange
from turtle import title
from typing import Optional
from certifi import contents
from fastapi import FastAPI,Request, Response, status, HTTPException, Form, Depends
from fastapi.params import Body
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models
from .database import SessionLocal, engine, get_db
from .inference import get_prediction

# models.Base.metadata.create_all(bind=engine)


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

class Post(BaseModel):
    input: str
    label: str
    prediction: float

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost',database='webapp',user='postgres',
#         password='123456', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("Connection to database failed")
#         print("Error: ", error)
#         time.sleep(2)

@app.get("/")
async def root(request: Request):
    data = {
        "page": "Home page"
    }
    # templates.
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

@app.post("/")
async def post(request: Request):
    try:
        formData = await request.form()
        print(formData['text'])
    except Exception as error:
        print("requset",error)
    data = get_prediction(formData['text'])[0]
    data['score'] =  round(data['score'] * 100,2)
    try:
        response = templates.TemplateResponse("page1.html", {"request": request,"input":formData['text'], "data": data})
        return response
    except Exception as error:
        # print(error)
        return {"status": "error"}
