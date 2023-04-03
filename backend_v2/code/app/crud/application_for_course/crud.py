from fastapi import APIRouter, Depends
from code.app.model.models import AdminModel
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from sqlalchemy import select

router = APIRouter(tags=['application for course'],
                   prefix='/api/v1/application',
                   responses={404: {"detail": "page not found"}})


@router.get('/', response_model=None)
async def get_all_app(db_session: Optional[AsyncSession] = None):
    result = await db_session.execute(select(AdminModel))
    return result.scalars().all()
