from fastapi import FastAPI
from Database import engine
import models
import crud
import auth

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(crud.router)
