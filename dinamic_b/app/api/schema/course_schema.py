import json
from typing import Optional

from pydantic import BaseModel


class Schema(BaseModel):
    title: str
    description: str
    type: str
    image_name: Optional[str] = None
    practice: int
    home_work: int
    project_portfolio: int
    sub_title: str
    visible: bool


class CourseReadSchema(BaseModel):
    id: int
    title: str
    description: str
    image_name: str
    type: str
    practice: int
    home_work: int
    project_portfolio: int
    visible: bool


    class Config:
        orm_mode = True


class CourseCreateSchema(Schema):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value
