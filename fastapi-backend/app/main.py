from fastapi import FastAPI,Header 
from typing import Optional
from pydantic import BaseModel

app=FastAPI()
@app.get("/")
def home():
    return {"message":"FastAPI running"}

@app.get("/health")
def health():
    return{"message":"yupp server is working "}


@app.get('/greet/{name}')
async def greet(name:str) -> dict:
    return{"message":f"hello {name}"}


@app.get("/greeet")
async def greeet(name:Optional[str]="User",age:int = 0) -> dict:
    return{"message":f"hello {name}","age":age }


class BookCreateModel(BaseModel):
    title:str
    author:str


@app.post("/create_book")
async def create_book(book_data:BookCreateModel):
    return {"title":book_data.title,
            "author":book_data.author
            }


@app.get("/get_header")
async def get_head(
    accept:str = Header(None),
    content_type:str = Header(None),
    user_agent:str=Header(None),
    host:str=Header(None)
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-type"]= content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host

    return request_headers