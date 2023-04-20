from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from code.course_applic.models import Application
from code.course_applic.schemas import CourseAppSchema
from code.db.database import get_async_session

router = APIRouter(
    prefix="/application",
    tags=["Course Application"]
)


@router.get("/")
async def course_root():
    return {"hello"}


@router.post('/create')
async def create_application(req: CourseAppSchema,
                             session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(Application).values(**req.dict())
        result = await session.execute(stmt)
        await session.commit()

        return {"status": "success"}
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={"status": "error",
                                    "data": None,
                                    "details": None})


@router.get("/list", response_model=List[CourseAppSchema])
async def list_application(id: int,
                           session: AsyncSession = Depends(get_async_session)):
    query = select(Application).where(Application.c.id == id)
    result = await session.execute(query)
    print(result.all())
    return result.all()
