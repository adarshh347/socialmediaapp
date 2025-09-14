from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
# Response
# with Response we can set custom headers, send different data formals(not just json or dictionary) and
# change the content type by telling the browser the response is pdf,image or sth else
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
# RealDictCursor gives column name through psycopg2 which is not automatically available
import time
# name of the route
app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published: bool=True
while True:
    try:
        conn=psycopg2.connect(host= 'localhost' ,database='fastapi' ,user='postgres' ,password='1234', cursor_factory =RealDictCursor)
        cursor=conn.cursor()
        print("database connection was successful!")
        break
    except Exception as error:
        print("connection to database failed")
        print("Error:", error)
        time.sleep(2)       #after two seconds it will try again to connect


@app.get('/')
async def root():
    return {'msg':'hello world'}
    # abc = "adarsh"
    # return abc

ds=['array','string','ll','dll']

@app.get('/reverse')
async def root():
    abc="adarsh"
    return {'msg': 'hello world'}
    # return abc
    # results={}
    # for i in range(len(ds)):
    #     results[i]=ds[i]
    # return results
