import os
from typing import List
from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, status
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from api.model.teacher_model import TeacherModel
from api.db.session import get_db
from api.schema.teacher_schema import TeacherCreateSchema, TeacherReadSchema
from auth.login import get_current_admin
from utils.teacher_logic import create_teacher_in_db, get_teacher_from_db, update_teacher_in_db
from utils.img_logic import upload_img, delete_old_image

router = APIRouter(
    tags=['teacher'],
    prefix='/api/home/teacher'
)


@router.get('/get-list', response_model=List[TeacherReadSchema])
async def get_teacher_list(db: Session = Depends(get_db),
                           login: dict = Depends(get_current_admin)
                           ):
    query = db.query(TeacherModel).all()
    if query is None:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )
    return query


@router.get('/get-by-id/{teacher_id}', response_model=TeacherReadSchema)
async def get_teacher_by_id(teacher_id: int,
                            db: Session = Depends(get_db),
                            login: dict = Depends(get_current_admin)
                            ):
    query = db.query(TeacherModel).filter(TeacherModel.id == teacher_id).first()
    if query is None:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )
    return query


@router.post('/create', response_model=TeacherReadSchema)
async def create_teacher_endpoint(teacher_data: TeacherCreateSchema,
                                  db: Session = Depends(get_db),
                                  login: dict = Depends(get_current_admin)
                                  ):
    teacher_model = create_teacher_in_db(teacher_data, db)
    return teacher_model


@router.post("/add-photo/{teacher_id}", response_model=TeacherReadSchema)
async def add_photo_to_teacher(teacher_id: int,
                               file: UploadFile = File(...),
                               db: Session = Depends(get_db),
                               login: dict = Depends(get_current_admin)
                               ):
    teacher_model = get_teacher_from_db(teacher_id, db)

    image = await upload_img(file)
    teacher_model.image = image

    db.commit()

    return teacher_model


@router.put("/update/{teacher_id}", response_model=TeacherReadSchema)
async def update_teacher(teacher_id: int,
                         teacher_data: TeacherCreateSchema,
                         db: Session = Depends(get_db),
                         login: dict = Depends(get_current_admin)
                         ):
    res = update_teacher_in_db(teacher_id, teacher_data, db)

    return res


@router.put("/update/image/{teacher_id}", response_model=TeacherReadSchema)
async def update_teacher_image(teacher_id: int,
                               file: UploadFile = File(...),
                               db: Session = Depends(get_db),
                               login: dict = Depends(get_current_admin)
                               ):
    teacher = db.query(TeacherModel).filter(TeacherModel.id == teacher_id).first()
    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    await delete_old_image(teacher.image)

    new_image = await upload_img(file)

    teacher.image = new_image

    db.commit()
    db.refresh(teacher)

    return teacher


@router.delete("/delete/{teacher_id}")
async def del_teacher(teacher_id: int,
                      db: Session = Depends(get_db),
                      login: dict = Depends(get_current_admin)
                      ):
    teacher = db.query(TeacherModel).filter(TeacherModel.id == teacher_id).first()

    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    await delete_old_image(teacher.image)

    db.delete(teacher)
    db.commit()

    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT,
        content="Teacher successfully deleted"
    )
