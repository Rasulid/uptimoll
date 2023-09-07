from pydantic import BaseModel


class RequestCreatechema(BaseModel):
    name: str
    course: str
    number: int
    processed: bool
    student: bool


class RequestReadSchema(BaseModel):
    id: int
    name: str
    course: str
    number: int
    processed: bool
    student: bool
