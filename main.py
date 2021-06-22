from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get("/blog/unpublished")
def unpublished():
    # This method needs to be below the about endpoint bcse fastapi read the endpoints in order
    return {'data': 'all unpublished blogs'}


@app.get("/blog/{id}")
def about(id: int):
    return {'data': id}


@app.get("/blog/{id}/comments")
def comments(id: int, limit: int = 10):
    return {'data': {'1', '2'}}
