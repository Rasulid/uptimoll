from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from api.db.DataBase import Base


class StudentWorkModel(Base):
    __tablename__ = 'student_work'
    id = Column(Integer, primary_key=True, index=True)
    link = Column(String)
    image_name = Column(String)
    visible = Column(Boolean)
    course_id = Column(Integer, ForeignKey('course.id', ondelete="CASCADE"))

    course_rel = relationship('CourseModel', back_populates="student_work_rel")
