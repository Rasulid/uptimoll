
from pydantic import BaseModel


class StudentWorkCreateSchema(BaseModel):
    link: str
    image_name: str
    visible: bool


class StudentWorkReadSchema(BaseModel):
    id: int
    link: str
    image_name: str
    visible: bool
    course_id: int

    class Config:
        orm_mode = True


class StudentWorkSiteSchema(BaseModel):
    link: str
    image_name: str
    visible: bool

    class Config:
        orm_mode = True