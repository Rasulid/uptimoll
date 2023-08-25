from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from api.db.session import get_db
from api.auth.login import get_current_admin, get_user_exceptions
from api.schema.student_work_schema import StudentWorkCreateSchema, StudentWorkReadSchema
from api.model.course_model import StudentWorkModel

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


@router.post("/create")
async def create(schema: StudentWorkCreateSchema, course_id: int,
                 db: Session = Depends(get_db)):
    # course_query

    model = StudentWorkModel()
    model.link = schema.link
    model.image_name = schema.image_name
    model.visible = schema.visible
    model.course_id = course_id

    db.add(model)
    db.commit()

    return model
