from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from api.db.session import get_db
from api.auth.login import get_current_admin
from api.schema.request_schema import RequestCreatechema, RequestReadSchema
from api.model.request_model import RequestModel

router = APIRouter(tags=["Request"],
                   prefix="/api/request")


@router.get("/get-list", response_model=List[RequestReadSchema])
async def get_list_formats(db: Session = Depends(get_db),
                           login: dict = Depends(get_current_admin)):
    query = db.query(RequestModel).all()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found"
        )
    return query


@router.get("/get-by-id/{request_id}", response_model=RequestReadSchema)
async def get_formats(request_id: int,
                      db: Session = Depends(get_db)):
    query = db.query(RequestModel).filter(RequestModel.id == request_id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    return query


@router.post("/create", response_model=RequestReadSchema)
async def create(schema: RequestReadSchema,
                 request_id: int,
                 db: Session = Depends(get_db),
                 login: dict = Depends(get_current_admin)):
    query = db.query(RequestModel).filter(RequestModel.id == request_id).first()
    if query is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Course not found")
    model = RequestModel()
    model.course = schema.course
    model.name = schema.name
    model.number = schema.number
    model.student = schema.student
    model.processed = schema.processed

    db.add(model)
    db.commit()

    return model



@router.put("/change-request/{request_id}", response_model=RequestReadSchema)
async def change_format(request_id: int,
                        schema: RequestCreatechema,
                        db: Session = Depends(get_db),
                        login: dict = Depends(get_current_admin)):
    query = db.query(RequestModel).filter(RequestModel.id == request_id).first()
    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found"
        )
    query.course = schema.course
    query.name = schema.name
    query.number = schema.number
    query.student = schema.student
    query.processed = schema.processed
    db.add(query)
    db.commit()
    return query


@router.delete("/delete-request/{request_id}")
async def del_format(request_id: int,
                     db: Session = Depends(get_db),
                     login: dict = Depends(get_current_admin)):
    query = db.query(RequestModel).filter(RequestModel.id == request_id).first()

    if query is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )
    db.delete(query)
    db.commit()
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT,
                        content="Successful")