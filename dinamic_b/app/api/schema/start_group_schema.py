import datetime
import time

from pydantic import BaseModel


class StartGroupCreateSchema(BaseModel):
    when_start: str
    when_start_ru: str

    group_lang: str
    group_lang_ru: str

    time_start: str
    time_start_ru: str

    time_end: str
    time_end_ru: str

    weeks: str
    weeks_ru: str

    course_id: int


class StartGroupReadSchema(StartGroupCreateSchema):
    id: int

    class Config:
        orm_mode = True


