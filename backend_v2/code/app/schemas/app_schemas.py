from pydantic import BaseModel


class ApplicationSchema(BaseModel):
    name: str
    course: str
    phone_number: str
