from fastapi import FastAPI
from routers import posts
from db import models
from db.database import engine


app = FastAPI()

app.include_router(posts.router)

models.Base.metadata.create_all(engine)

