from fastapi import APIRouter

router = APIRouter(
    prefix="/application",
    tags=["Course Application"]
)


@router.get("/")
async def course_root():
    return {"hello"}