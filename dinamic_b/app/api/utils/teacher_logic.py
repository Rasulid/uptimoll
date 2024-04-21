from fastapi import HTTPException
from sqlalchemy.orm import Session

from api.model.teacher_model import TeacherModel
from api.schema.teacher_schema import TeacherCreateSchema


def create_teacher_in_db(teacher_data: TeacherCreateSchema, db: Session) -> TeacherModel:

    teacher_data.image = "start"
    teacher_model = TeacherModel(**teacher_data.model_dump())
    db.add(teacher_model)
    db.commit()
    return teacher_model


def get_teacher_from_db(teacher_id: int, db: Session) -> TeacherModel:

    teacher_model = db.query(TeacherModel).filter(TeacherModel.id == teacher_id).first()

    if not teacher_model:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher_model


def update_teacher_in_db(teacher_id: int, teacher_data: TeacherCreateSchema, db: Session):
    teacher = db.query(TeacherModel).filter(TeacherModel.id == teacher_id).first()
    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )
    teacher.name = teacher_data.name
    teacher.description = teacher_data.description
    teacher.course = teacher_data.course
    teacher.image = teacher_data.image

    db.commit()
    db.refresh(teacher)

    return teacher
