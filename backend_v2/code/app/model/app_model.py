from .base_model import BaseModel
from sqlalchemy import Integer, String, Column


class AppModel(BaseModel):
    __tablename__ = "app"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    course = Column(String)
    phone_number = Column(String)