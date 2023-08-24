
from pydantic import BaseModel


class LearningFormatCreateSchema(BaseModel):
    group: str
    desc: str
    desc_2: str
    price: int
    course_id: int


class LearningFormatReadSchema(BaseModel):
    id: int
    group: str
    desc: str
    desc_2: str
    price: int
    course_id: int

    class Config:
        orm_mode = True
