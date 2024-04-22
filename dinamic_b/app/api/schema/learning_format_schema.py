from pydantic import BaseModel


class LearningFormatCreateSchema(BaseModel):
    group: str
    group_ru: str

    desc: str
    desc_ru: str

    desc_2: str
    desc_2_ru: str

    price: str

    course_id: int


class LearningFormatReadSchema(LearningFormatCreateSchema):
    id: int

    class Config:
        orm_mode = True


