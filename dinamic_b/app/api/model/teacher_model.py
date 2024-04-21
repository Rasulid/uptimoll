from sqlalchemy import *
from .base_model import BaseModel


class TeacherModel(BaseModel):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    course = Column(String, nullable=False)
    image = Column(String, nullable=False)
    description = Column(String, nullable=False)

