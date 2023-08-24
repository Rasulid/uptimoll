import datetime
import time


from pydantic import BaseModel


class StartGroupCreateSchema(BaseModel):
    when_start: str
    group_lang: str
    time_start: str
    time_end: str
    weeks: str


class StartGrupReadSchema(BaseModel):
    id: int
    when_start: str
    group_lang: str
    time_start: str
    time_end: str
    weeks: str

    class Config:
        orm_mode = True
