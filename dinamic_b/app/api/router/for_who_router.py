from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from api.db.session import get_db
from api.auth.login import get_current_admin, get_user_exceptions
from api.model.course_model import ForWhoModel, CourseModel
from api.schema.for_who_schema import ForWhoCreateSchema, ForWhoReadSchema

router = APIRouter(tags=["For who"],
                   prefix="/api/for-who")


@router.get('/get-list', response_model=List[ForWhoReadSchema])
async def get_list(db: Session = Depends(get_db),
                   login: dict = Depends(get_current_admin)):
    query = db.query(ForWhoModel).all()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Something is wrong Selecting DataBase"
        )
    return query


@router.get('/get-by-id/{for_who_id}', response_model=ForWhoReadSchema)
async def get_by_id(for_who_id: int,
                    db: Session = Depends(get_db),
                    login: dict = Depends(get_current_admin)):
    query = db.query(ForWhoModel).filter(ForWhoModel.id == for_who_id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found"
        )
    return query


@router.post('/create', response_model=ForWhoReadSchema)
async def create(schema: ForWhoCreateSchema,
                 course_id: int,
                 db: Session = Depends(get_db),
                 # login: dict = Depends(get_current_admin)
                 ):
    query = db.query(CourseModel).filter(CourseModel.id == course_id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )

    schema.course_id = course_id
    model = ForWhoModel(**schema.model_dump())

    db.add(model)
    db.commit()

    return model


@router.put("/change-for-who/{id}", response_model=ForWhoReadSchema)
async def change_for_who(id: int,
                         schema: ForWhoCreateSchema,
                         db: Session = Depends(get_db),
                         login: dict = Depends(get_current_admin)):
    query = db.query(ForWhoModel).filter(ForWhoModel.id == id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found"
        )
    query.title = schema.title
    query.description = schema.description

    db.add(query)
    db.commit()
    return query


@router.delete("/delete-course/{id}", response_model=ForWhoReadSchema)
async def del_for_who(id: int,
                      db: Session = Depends(get_db),
                      login: dict = Depends(get_current_admin)):
    query = db.query(ForWhoModel).filter(ForWhoModel.id == id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found"
        )
    db.delete(query)
    db.commit()
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT,
                        content="Successful")
