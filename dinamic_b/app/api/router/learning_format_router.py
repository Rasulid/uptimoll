from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from api.db.session import get_db
from api.auth.login import get_current_admin, get_user_exceptions
from api.schema.learning_format_schema import LearningFormatCreateSchema, LearningFormatReadSchema
from api.model.course_model import LearningFormatModel, CourseModel

router = APIRouter(tags=["learning format"],
                   prefix="/api/learning-format")


@router.get("/get-list", response_model=List[LearningFormatReadSchema])
async def get_list_formats(db: Session = Depends(get_db),
                           login: dict = Depends(get_current_admin)):
    query = db.query(LearningFormatModel).all()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    return query


@router.get("/get-by-id/{format_id}", response_model=LearningFormatReadSchema)
async def get_formats(format_id: int,
                      db: Session = Depends(get_db),
                      login: dict = Depends(get_current_admin)):
    query = db.query(LearningFormatModel).filter(LearningFormatModel.id == format_id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    return query


@router.post("/create", response_model=LearningFormatReadSchema)
async def create(schema: LearningFormatCreateSchema,
                 course_id: int,
                 db: Session = Depends(get_db),
                 # login: dict = Depends(get_current_admin)
                 ):
    # course_query
    query = db.query(CourseModel).filter(CourseModel.id == course_id).first()
    if query is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Course not found")

    schema.course_id = course_id
    model = LearningFormatModel(**schema.model_dump())


    db.add(model)
    db.commit()

    return model


@router.put("/change-format/{format_id}", response_model=LearningFormatReadSchema)
async def change_format(format_id: int,
                        schema: LearningFormatCreateSchema,
                        db: Session = Depends(get_db),
                        login: dict = Depends(get_current_admin)):
    query = db.query(LearningFormatModel).filter(LearningFormatModel.id == format_id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Format not found"
        )
    query.group = schema.group
    query.desc = schema.desc
    query.desc_2 = schema.desc_2
    query.price = schema.price

    db.add(query)
    db.commit()
    return query


@router.delete("/delete-format/{format_id}")
async def del_format(format_id: int,
                     db: Session = Depends(get_db),
                     login: dict = Depends(get_current_admin)):
    query = db.query(LearningFormatModel).filter(LearningFormatModel.id == format_id).first()

    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    db.delete(query)
    db.commit()
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT,
                        content="Successful")
