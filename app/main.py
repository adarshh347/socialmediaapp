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

my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favorite foods", "content": "I like pizza", "id": 2}
]
@app.get("/postss")
def get_posts():
    cursor.execute("""  SELECT * FROM POSTS """)
    posts=cursor.fetchall()
    print(posts)
    return {"data": posts}

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    # important line below: how to create new rows in database through the code itself using cursor command
    cursor.execute(f"INSERT INTO posts(title, content, published) VALUES( {post.title}, {post.content}, {post.published} )")

    # second way below
    # cursor.execute(""" INSERT INTO posts(title, content, published) VALUES (%s,%s,%s) """, (post.title, post.content, post.published))

    post_dict=post.dict()
    post_dict['id']=randrange(0,10000000)
    my_posts.append(post_dict)
    return {"data": post_dict}
