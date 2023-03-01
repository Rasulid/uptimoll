from fastapi import FastAPI, Depends, Body
from sqlalchemy.orm import Session
import models
from Database import engine, SessionLocal
import auth
from auth import get_current_user, get_user_exceptions
from schemas import InfoOut


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)


@app.get("/")
async def get_msg(db: Session = Depends(get_db),
                  user: dict = Depends(get_current_user)):
    result = []
    if user is None:
        raise get_user_exceptions()
    query = db.query(models.UserInfo).all()
    for info in query:
        result.append(InfoOut(name=info.name,
                              course=info.course,
                              phone_number=info.phone_number))
    return result


@app.post("/")
async def post_req(name: str = Body(...),
                   course: str = Body(...),
                   phone_number: str = Body(...),
                   db: Session = Depends(get_db),
                   user: dict = Depends(get_current_user)):
    if user is None:
        raise get_user_exceptions()

    model = models.UserInfo()

    model.name = name
    model.course = course
    model.phone_number = phone_number

    db.add(model)
    db.commit()

    return "Success"



