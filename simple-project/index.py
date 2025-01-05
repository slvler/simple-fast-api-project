from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/index")
def index():
    return { "hello": "world" }


@app.get('/show/{show_id}')
def show(show_id):
    return {"data": "show_id:" + show_id}

@app.get("/publish/{id}")
def publish(id: int):
    return {"data": id}

@app.get("/pub/{text}")
def publish(text: str):
    return {"data": text}

#query parameters
@app.get("/list")
def list(limit, published: bool = True):
    print(published)
    return {"data": f'{limit} list func'}

@app.get("/optional-parameters")
def optional_parameter(name: str, sort: Optional[str] = None):
    print(sort)
    return {"hello": "world"}

#Path parameters
@app.get("/detail/{id}/show")
def detail(id):
    return {"data": {1,2,3,4,5, id}}



class createItem(BaseModel):
    name: str
    content: str
    vote: int
    status: bool

#request body
@app.post("/hello")
def create(request: createItem):
    print(request.name)
    print(request.content)
    print(request.vote)
    print(request.status)
    return request
