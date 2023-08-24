
from pydantic import BaseModel


class CourseCreateSchema(BaseModel):
    title: str
    description: str
    type: str
    image_name: str
    practice: int
    home_work: int
    project_portfolio: int
    for_who_photo: str
    visible: bool


class CourseReadSchema(BaseModel):
    id: int
    title: str
    description: str
    type: str
    image_name: str
    practice: int
    home_work: int
    project_portfolio: int
    for_who_photo: str
    visible: bool

    class Config:
        orm_mode = True
