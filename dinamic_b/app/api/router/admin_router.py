from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from api.db.session import get_db
from api.auth.admin_auth import password_hash
from api.auth.login import get_current_admin, get_user_exceptions
from api.schema.admin_schema import Admin_Schema, Admin_Read_Schema
from api.model.admin_model import AdminModel

router = APIRouter(prefix="/api/admin",
                   tags=['admin'])


@router.post("/registr", response_model=List[Admin_Read_Schema])
async def register(admin: Admin_Schema,
                   db: Session = Depends(get_db),
                   # login: dict = Depends(get_current_admin)
                   ):
    res = []
    admin.created_at = datetime.utcnow()
    admin_model = AdminModel(**admin.model_dump())

    if admin_model:
        user_name = db.query(AdminModel).all()
        for x in user_name:
            if admin_model.gmail == x.gmail:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                    detail={'msg': f"{admin_model.gmail} user is already exists"})
    hash_password = password_hash(admin.password)
    admin_model.password = hash_password

    res.append(admin_model)

    db.add(admin_model)
    db.commit()

    return res


@router.put("/update/{id}")
async def update_admin(id: int
                       , admin: Admin_Schema,
                       db: Session = Depends(get_db),
                       login: dict = Depends(get_current_admin)):
    admin_model = db.query(AdminModel) \
        .filter(AdminModel.id == id).first()

    if admin_model is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Admin not found"})

    admin_model.name = admin.name
    admin_model.born = admin.born
    admin_model.created_at = datetime.utcnow()
    admin_model.phone_number = admin.phone_number
    admin_model.gmail = admin.gmail
    admin_model.password = admin.password
    admin_model.country = admin.country
    admin_model.region = admin.region
    admin_model.is_active = admin.is_active
    admin_model.is_staff = admin.is_staff
    admin_model.is_superuser = admin.is_superuser
    admin_model.is_verified = admin.is_verified

    db.add(admin_model)
    db.commit()

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": f"Update admin {admin_model.gmail} was successfully"})


@router.get("/admins-list", response_model=List[Admin_Read_Schema])
async def admin_list(db: Session = Depends(get_db),
                     user: dict = Depends(get_current_admin)):
    if user is None:
        raise get_user_exceptions()

    model_ = db.query(AdminModel).all()
    return model_


@router.get("/{id}", response_model=Admin_Read_Schema)
async def admin_by_ID(id: int, db: Session = Depends(get_db),
                      user: dict = Depends(get_current_admin)):
    db_query = db.query(AdminModel) \
        .filter(AdminModel.id == id).first()

    if db_query is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Admin not found"})

    return db_query


@router.delete("/delete/{id}")
async def delete_admin(id: int,
                       db: Session = Depends(get_db),
                       login: dict = Depends(get_current_admin)):
    db_query = db.query(AdminModel) \
        .filter(AdminModel.id == id).first()

    if db_query is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Admin not found"})

    delete = db.query(AdminModel).filter(AdminModel.id == id).delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/get-user-me/", response_model=Admin_Read_Schema)
async def get_user_me(db: Session = Depends(get_db),
                      current_user: dict = Depends(get_current_admin)):
    user_id = current_user.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User ID not found in token")

    user = db.query(AdminModel).filter(AdminModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user
