from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from api.db.session import get_db
from api.auth.login import get_current_admin, get_user_exceptions
from api.schema.learning_format_schema import LearningFormatCreateSchema, LearningFormatReadSchema
from api.model.course_model import LearningFormatModel

router = APIRouter(tags=["learnong format"],
                   prefix="/api/learning-format")


@router.get("/get-list", response_model=List[LearningFormatReadSchema])
async def get_list_groups(db: Session = Depends(get_db)):
    query = db.query(LearningFormatModel).all()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Something is wrong Selecting DataBase"
        )
    return query


@router.post("/create")
async def create(schema: LearningFormatCreateSchema, course_id: int,
                 db: Session = Depends(get_db)):
    # course_query

    model = LearningFormatModel()
    model.group = schema.group
    model.desc = schema.desc
    model.desc_2 = schema.desc_2
    model.price = schema.price
    model.course_id = course_id

    db.add(model)
    db.commit()

    return model
