from pydantic import BaseModel


class TeacherCreateSchema(BaseModel):
    name: str
    name_ru: str

    image: str

    course: str
    course_ru: str

    description: str
    description_ru: str


    class Config:
        orm_mode = True


class TeacherReadSchema(TeacherCreateSchema):
    id: int

    class Config:
        orm_mode = True

