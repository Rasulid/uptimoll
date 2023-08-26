from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from api.db.session import get_db
from api.auth.login import get_current_admin, get_user_exceptions
from api.schema.start_group_schema import StartGroupCreateSchema, StartGroupReadSchema
from api.model.course_model import StartGroupModel, CourseModel

router = APIRouter(tags=["group start"],
                   prefix="/api/group-start")


@router.get("/get-list", response_model=List[StartGroupReadSchema])
async def get_list_groups(db: Session = Depends(get_db)):
    query = db.query(StartGroupModel).all()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Groups not found"
        )
    return query


@router.get("/get-by-id/{group_id}", response_model=StartGroupReadSchema)
async def get_list_groups(group_id: int,
                          db: Session = Depends(get_db)):
    query = db.query(StartGroupModel).filter(StartGroupModel.id == group_id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Group not found"
        )
    return query


@router.post("/create", response_model=StartGroupReadSchema)
async def create(schema: StartGroupCreateSchema,
                 course_id: int,
                 db: Session = Depends(get_db)):
    # course_query
    query = db.query(CourseModel).filter(CourseModel.id == course_id).first()
    if query is None:
        if query is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )
    model = StartGroupModel()
    model.when_start = schema.when_start
    model.weeks = schema.weeks
    model.group_lang = schema.group_lang
    model.time_start = schema.time_start
    model.time_end = schema.time_end
    model.weeks = schema.weeks
    model.course_id = course_id

    db.add(model)
    db.commit()

    return model


@router.put("/change-course/{course_id}", response_model=StartGroupReadSchema)
async def change_start_group(course_id: int,
                             schema: StartGroupCreateSchema,
                             db: Session = Depends(get_db)):
    query = db.query(StartGroupModel).filter(StartGroupModel.id == course_id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    query.when_start = schema.when_start
    query.group_lang = schema.group_lang
    query.time_start = schema.time_start
    query.time_end = schema.time_end
    query.weeks = schema.weeks

    db.add(query)
    db.commit()
    return query


@router.delete("/delete-start-group/{group_id}")
async def del_start_group(group_id: int,
                     db: Session = Depends(get_db)):
    query = db.query(StartGroupModel).filter(StartGroupModel.id == group_id).first()

    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    db.delete(query)
    db.commit()
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT,
                        content="Successful")
