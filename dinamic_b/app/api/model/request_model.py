from sqlalchemy import Column, String, Boolean, Integer
from api.db.DataBase import Base


class RequestModel(Base):
    __tablename__ = 'request'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    course = Column(String)
    number = Column(String)
    processed = Column(Boolean)
    student = Column(Boolean)