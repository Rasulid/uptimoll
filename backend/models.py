from Database import Base
from sqlalchemy import Integer, String, Column


class UserInfo(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    course = Column(String)
    phone_number = Column(String)


class Admin(Base):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
