from sqlalchemy import *
from api.db.DataBase import Base


class TeacherModel(Base):
    __tablename__ = 'teacher'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    image = Column(String, nullable=False)
    description = Column(String, nullable=False)

