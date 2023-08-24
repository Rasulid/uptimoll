from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from api.db.session import get_db
from api.auth.login import get_current_admin, get_user_exceptions
from api.schema.start_group_schema import StartGroupCreateSchema, StartGrupReadSchema
from api.model.course_model import StartGroupModel

router = APIRouter(tags=["group start"],
                   prefix="/api/group-start")


@router.get("/get-list", response_model=List[StartGrupReadSchema])
async def get_list_groups(db: Session = Depends(get_db)):
    query = db.query(StartGroupModel).all()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Something is wrong Selecting DataBase"
        )
    return query


@router.post("/create")
async def create(schema: StartGroupCreateSchema, course_id: int,
                 db: Session = Depends(get_db)):
    # course_query

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
