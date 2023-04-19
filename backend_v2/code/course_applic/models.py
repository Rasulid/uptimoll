from sqlalchemy import Column, String, Integer, DATE, MetaData
from datetime import datetime
from code.db.database import BASE

metadata = MetaData()
class Application(BASE):
    __tablename__ = "app"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    course = Column(String)
    phone_number = Column(String)
    send_date = Column(DATE)

