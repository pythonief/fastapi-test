from fastapi import FastAPI

from blog import models
from blog.routers import user

from .database import engine
from .routers import blog

app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)

models.Base.metadata.create_all(engine)
