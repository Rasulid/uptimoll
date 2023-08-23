from sqlalchemy import Column, String, Integer, ForeignKey, Time
from sqlalchemy.orm import relationship
from api.db.DataBase import Base


class StartGroupModel(Base):
    __tablename__ = 'start_group'  # Исправлено здесь
    id = Column(Integer, primary_key=True, index=True)
    when = Column(String)
    group_lang = Column(String)
    time_start = Column(Time)
    time_end = Column(Time)
    weeks = Column(String)
    course_id = Column(Integer, ForeignKey("course.id", ondelete="CASCADE"))

    course_rel = relationship('CourseModel', back_populates="start_group_rel")

