from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File
from sqlalchemy.orm import Session, joinedload
from starlette.responses import JSONResponse

from api.db.session import get_db
from api.auth.login import get_current_admin
from api.model.course_model import CourseModel
from api.schema.course_schema import CourseReadSchema, Schema
from api.utils.course_logic import update_course_image
from api.utils.img_logic import upload_img, delete_old_image

router = APIRouter(tags=["Course"],
                   prefix="/api/course")


@router.get('/get-list', response_model=List[CourseReadSchema])
async def get_list(db: Session = Depends(get_db),
                   # login: dict = Depends(get_current_admin)
                   ):
    query = db.query(CourseModel).all()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Something is wrong Selecting DataBase"
        )
    return query


@router.get('/get-course/{course_id}')
async def get_course(course_id: int,
                     db: Session = Depends(get_db)
                     ):
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


@router.post('/create', response_model=CourseReadSchema)
async def create(course_schema: Schema,
                 db: Session = Depends(get_db),
                 login: dict = Depends(get_current_admin)
                 ):
    course_schema.image_name = 'start'
    model = CourseModel(**course_schema.model_dump())

    db.add(model)
    db.commit()

    return model


@router.post("/add-photo/{course_id}", response_model=CourseReadSchema)
async def add_photo(course_id: int,
                    file: UploadFile = File(...),
                    db: Session = Depends(get_db),
                    login: dict = Depends(get_current_admin)
                    ):
    model = db.query(CourseModel).filter(CourseModel.id == course_id).first()
    if model is None:
        raise HTTPException(status_code=404,
                            detail="Course not found")
    image = await upload_img(file)
    model.image_name = image

    db.add(model)
    db.commit()

    return model


@router.put("/change-course/{course_id}", response_model=CourseReadSchema)
async def change_course(course_id: int,
                        schema: Schema,
                        db: Session = Depends(get_db),
                        login: dict = Depends(get_current_admin)
                        ):
    query = db.query(CourseModel).filter(CourseModel.id == course_id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    query.title = schema.title
    query.title_ru = schema.title_ru

    query.description = schema.description
    query.description_ru = schema.description_ru

    query.type = schema.type
    query.type_ru = schema.type_ru

    query.image_name = query.image_name
    query.practice = schema.practice
    query.home_work = schema.home_work
    query.project_portfolio = schema.project_portfolio
    query.visible = schema.visible

    query.sub_title = schema.sub_title
    query.sub_title_ru = schema.sub_title_ru

    db.add(query)
    db.commit()
    return query


@router.put('/update-image/{cource_id}')
async def update_image(course_id: int,
                       file: UploadFile = File(...),
                       db: Session = Depends(get_db),
                       login: dict = Depends(get_current_admin)
                       ):
    course = await update_course_image(course_id, file, db)

    return course


@router.delete("/delete-course/{course_id}")
async def del_course(course_id: int,
                     db: Session = Depends(get_db),
                     login: dict = Depends(get_current_admin)
                     ):
    query = db.query(CourseModel).filter(CourseModel.id == course_id).first()

    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )

    await delete_old_image(query.image_name)

    db.delete(query)
    db.commit()
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT,
                        content="Successful")
