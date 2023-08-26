import datetime
import time

from pydantic import BaseModel


class StartGroupCreateSchema(BaseModel):
    when_start: str
    group_lang: str
    time_start: str
    time_end: str
    weeks: str


class StartGroupReadSchema(BaseModel):
    id: int
    when_start: str
    group_lang: str
    time_start: str
    time_end: str
    weeks: str
    course_id: int

    class Config:
        orm_mode = True


class StartGroupSiteSchema(BaseModel):
    when_start: str
    group_lang: str
    time_start: str
    time_end: str
    weeks: str

    class Config:
        orm_mode = True
