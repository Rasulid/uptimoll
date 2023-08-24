from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from api.db.session import get_db
from api.auth.login import get_current_admin, get_user_exceptions
from api.model.course_model import ForWhoModel
from schema.for_who_schema import ForWhoCreateSchema

router = APIRouter(tags=["For who"],
                   prefix="/api/for-who")


@router.get('/get-list')
async def get_list(db: Session = Depends(get_db)):
    query = db.query(ForWhoModel).all()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Something is wrong Selecting DataBase"
        )
    return query


@router.post('/create')
async def create(schema: ForWhoCreateSchema
                 , db: Session = Depends(get_db)):
    model = ForWhoModel()
    model.title = schema.title
    model.sub_title = schema.sub_title
    model.description = schema.description


    db.add(model)
    db.commit()

    return model
