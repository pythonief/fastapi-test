from fastapi import FastAPI

app = FastAPI()


@app.get("/", description='Some description')
async def index():
    return {'data': {'name': 'Ilan'}}


# This method needs to be below the about endpoint bcse fastapi read the endpoints in order
@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get("/blog/{id}")
def about(id: int):
    return {'data': id}


@app.get("/blog/{id}/comments")
def comments(id: int):
    return {'data': {'1', '2'}}
