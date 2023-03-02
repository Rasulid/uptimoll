from fastapi import APIRouter, Depends, Body
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


router = APIRouter()
models.Base.metadata.create_all(bind=engine)



@router.get("/")
async def get_msg(db: Session = Depends(get_db),
                  user: dict = Depends(get_current_user)):

    if user is None:
        raise get_user_exceptions()
    query = db.query(models.UserInfo).all()

    return query


@router.post("/")
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


@router.delete("/info")
async def delete_clients_info(info_id: int,
                              db: Session = Depends(get_db),
                              user: dict = Depends(get_current_user)):
    if user is None:
        raise get_user_exceptions()

    info_model = db.query(models.UserInfo) \
        .filter(models.UserInfo.id == info_id) \
        .delete()

    db.commit()

    return info_model

