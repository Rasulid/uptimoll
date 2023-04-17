from fastapi import APIRouter

router = APIRouter(prefix="/site",
                   tags=["site"],
                   responses={404: {"description": "Page not found"}})


@router.get('/')
async def read_root():
    return {"message": "Hello Site!"}
