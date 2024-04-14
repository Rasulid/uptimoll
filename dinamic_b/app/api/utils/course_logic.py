from fastapi import UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Type, Any

from model.course_model import CourseModel
from utils.img_logic import delete_old_image, upload_img

ModelType = Type['ModelType']


async def update_course_image(course_id: int,
                              file: UploadFile,
                              db: Session) -> HTTPException | Any:
    course = db.query(CourseModel).filter(CourseModel.id == course_id).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    if course.image_name:
        try:
            await delete_old_image(course.image_name)
        except Exception as e:
            return HTTPException(
                status_code=404,
                detail="course image not found"
            )

    new_image = await upload_img(file)

    course.image_name = new_image

    db.commit()
    db.refresh(course)

    return course
