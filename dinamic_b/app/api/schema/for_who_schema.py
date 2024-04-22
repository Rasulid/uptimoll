from pydantic import BaseModel


class ForWhoCreateSchema(BaseModel):
    title: str
    title_ru: str

    description: str
    description_ru: str

    course_id: int


class ForWhoReadSchema(ForWhoCreateSchema):
    id: int

    class Config:
        orm_mode = True

