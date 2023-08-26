import shutil
import uuid
from typing import List

from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File
from fastapi.responses import Response
from sqlalchemy.orm import Session, joinedload
from starlette.responses import JSONResponse

from api.db.session import get_db
from api.auth.login import get_current_admin, get_user_exceptions
from api.model.course_model import (CourseModel, StudentWorkModel,
                                    LearningFormatModel,ForWhoModel,StartGroupModel)
from api.schema.course_schema import CourseCreateSchema, CourseReadSchema

router = APIRouter(tags=["Course"],
                   prefix="/api/course")


async def upload_img(img: UploadFile = File(...)):
    img.filename = f"{uuid.uuid4()}.jpg"
    with open(f"static/image/{img.filename}", "wb") as buffer:
        shutil.copyfileobj(img.file, buffer)
    return img.filename


@router.get('/get-list')
async def get_list(db: Session = Depends(get_db)):
    query = db.query(CourseModel).all()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Something is wrong Selecting DataBase"
        )
    return query


@router.post('/create', response_model=CourseReadSchema)
async def create(course_schema: CourseCreateSchema,
                 db: Session = Depends(get_db)
                 ):
    model = CourseModel()
    model.title = course_schema.title
    model.description = course_schema.description
    model.type = course_schema.type
    model.image_name = "string"
    model.practice = course_schema.practice
    model.home_work = course_schema.home_work
    model.project_portfolio = course_schema.project_portfolio
    model.visible = course_schema.visible

    db.add(model)
    db.commit()

    return model


@router.post("/add-photo/{course_id}")
async def add_photo(course_id: int,
                    file: UploadFile = File(...),
                    db: Session = Depends(get_db)):
    model = db.query(CourseModel).filter(CourseModel.id == course_id).first()
    image = await upload_img(file)

    model.image_name = image

    db.add(model)
    db.commit()

    return "Success"


@router.get('/get-course/{course_id}')
async def get_course(course_id: int, db: Session = Depends(get_db)):
    course = (
        db.query(CourseModel)
        .filter(CourseModel.id == course_id)
        .options(
            joinedload(CourseModel.for_who_rel),
            joinedload(CourseModel.start_group_rel),
            joinedload(CourseModel.learn_format_rel),
            joinedload(CourseModel.student_work_rel)
        )
        .first()
    )

    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )

    return course
