from fastapi import APIRouter, Depends
from code.app.db.database import async_session
from code.app.model.admin_model import AdminModel
from code.app.model.app_model import AppModel
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from sqlalchemy import select
from code.app.schemas.app_schemas import ApplicationSchema

router = APIRouter(tags=['application for course'],
                   prefix='/api/v1/application',
                   responses={404: {"detail": "page not found"}})


# @router.get('/', response_model=None)
# async def get_all_app():
#     db = async_session()
#     result = await db.execute(select(AdminModel))
#     return result.scalars().all()


@router.get("/")
async def get_all_app():
    db = async_session()
    result = await db.execute(select(AppModel))
    return result.scalars().all()


@router.post("create/")
async def create(schema: ApplicationSchema):
    db = async_session()
    model = AppModel()
    model.name = schema.name
    model.course = schema.course
    model.phone_number = schema.phone_number

    db.add(model)
    db.commit()

    return 'Success'
