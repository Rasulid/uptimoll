from typing import Optional

from pydantic import BaseModel


class Schema(BaseModel):
    title: str
    title_ru: str

    description: str
    description_ru: str

    type: str
    type_ru: str

    image_name: Optional[str] = None

    practice: int
    home_work: int
    project_portfolio: int

    sub_title: str
    sub_title_ru: str

    visible: bool


class CourseReadSchema(Schema):
    id: int

    class Config:
        orm_mode = True

