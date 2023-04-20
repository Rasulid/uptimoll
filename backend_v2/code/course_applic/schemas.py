from datetime import datetime
from pydantic import BaseModel


class CourseAppSchema(BaseModel):
    name: str
    course: str
    phone_number: str
    send_date: datetime

    class Config:
        orm_mode = True
