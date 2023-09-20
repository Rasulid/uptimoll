from pydantic import BaseModel


class ForWhoCreateSchema(BaseModel):
    title: str
    description: str


class ForWhoReadSchema(BaseModel):
    id: int
    title: str
    sub_title: str
    description: str
    course_id: int

    class Config:
        orm_mode = True


class ForWhoSiteSchema(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True
