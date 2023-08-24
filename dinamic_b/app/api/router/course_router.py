from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from api.db.session import get_db
from api.auth.login import get_current_admin, get_user_exceptions
from api.model.course_model import CourseModel
from schema.course_schema import CourseCreateSchema

router = APIRouter(tags=["Course"],
                   prefix="/api/course")


@router.get('/get-list')
async def get_list(db: Session = Depends(get_db)):
    query = db.query(CourseModel).all()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Something is wrong Selecting DataBase"
        )
    return query


@router.post('/create')
async def create(schema: CourseCreateSchema
                 , db: Session = Depends(get_db)):
    model = CourseModel()
    model.title = schema.title
    model.description = schema.description
    model.type = schema.type
    model.image_name = schema.image_name
    model.practice = schema.practice
    model.home_work = schema.home_work
    model.project_portfolio = schema.project_portfolio
    model.for_who_photo = schema.for_who_photo
    model.visible = schema.visible

    db.add(model)
    db.commit()

    return model
