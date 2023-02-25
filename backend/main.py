from fastapi import FastAPI, Depends, Body
from sqlalchemy.orm import Session

import models
from Database import engine, SessionLocal


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def get_msg(db: Session = Depends(get_db)):
    return db.query(models.UserInfo).all()


@app.post("/")
async def post_req(name: str = Body(...),
                   course: str = Body(...),
                   phone_number: str = Body(...),
                   db: Session = Depends(get_db)):
    model = models.UserInfo()

    model.name = name
    model.course = course
    model.phone_number = phone_number

    db.add(model)
    db.commit()

    return "Success"


# @app.post("/check", tags=["admin"])
# async def check_admin(username: str,
#                       password: str,
#                       db: Session = Depends(get_db)):
#     if username and password:
#         model = db.query(models.Admin).all()
#         for x in model:
#             if username == x.username and password == x.password:
#                 return True
#
#     return False
