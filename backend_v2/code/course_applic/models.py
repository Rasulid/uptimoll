from sqlalchemy import Column, String, Integer, DATE, MetaData
from datetime import datetime
from code.db.Base_model import BaseModel

metadata = MetaData()


class Application(BaseModel):
    __tablename__ = "app"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    course = Column(String)
    phone_number = Column(String)
    send_date = Column(DATE)
