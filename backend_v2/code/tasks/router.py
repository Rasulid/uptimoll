from fastapi import APIRouter


router = APIRouter(prefix="/tasks",
                   tags=["tasks"],
                   responses={404: {"description": "Page Not Found"}})

@router.get("/")
async def read_tasks():
    return {"message": "hello tasks"}