from pydantic import BaseModel


class TeacherCreateSchema(BaseModel):
    name: str
    image: str
    course: str
    description: str

    class Config:
        orm_mode = True


class TeacherReadSchema(BaseModel):
    id: int
    name: str
    course: str
    image: str
    description: str

    class Config:
        orm_mode = True

