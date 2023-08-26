from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from api.db.session import get_db
from api.auth.login import get_current_admin, get_user_exceptions
from api.schema.student_work_schema import StudentWorkCreateSchema, StudentWorkReadSchema
from api.model.course_model import StudentWorkModel, CourseModel

router = APIRouter(tags=["student work"],
                   prefix="/api/student-work")


@router.get("/get-list", response_model=List[StudentWorkReadSchema])
async def get_list_groups(db: Session = Depends(get_db)):
    query = db.query(StudentWorkModel).all()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Something is wrong Selecting DataBase"
        )
    return query


@router.get("/get-by-id/{work_id}", response_model=StudentWorkReadSchema)
async def get_by_id(work_id: int,
                    db: Session = Depends(get_db)):
    query = db.query(StudentWorkModel).filter(StudentWorkModel.id == work_id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Work not found"
        )
    return query


@router.post("/create", response_model=StudentWorkReadSchema)
async def create(schema: StudentWorkCreateSchema, course_id: int,
                 db: Session = Depends(get_db)):
    # course_query
    query = db.query(CourseModel).filter(CourseModel.id == course_id).first()
    if query is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Course not found")
    model = StudentWorkModel()
    model.link = schema.link
    model.image_name = schema.image_name
    model.visible = schema.visible
    model.course_id = course_id

    db.add(model)
    db.commit()

    return model


@router.put("/change-work/{work_id}", response_model=StudentWorkReadSchema)
async def change_work(work_id: int,
                      schema: StudentWorkCreateSchema,
                      db: Session = Depends(get_db)):
    query = db.query(StudentWorkModel).filter(StudentWorkModel.id == work_id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Work not found"
        )
    query.link = schema.link
    query.image_name = schema.image_name
    query.visible = schema.visible

    db.add(query)
    db.commit()
    return query


@router.delete("/delete-work/{work_id}")
async def del_work(work_id: int,
                     db: Session = Depends(get_db)):
    query = db.query(StudentWorkModel).filter(StudentWorkModel.id == work_id).first()

    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Work not found"
        )
    db.delete(query)
    db.commit()
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT,
                        content="Successful")
