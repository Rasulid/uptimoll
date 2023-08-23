from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from api.db.DataBase import Base

from .for_who_model import ForWhoModel
from .start_group_model import StartGroupModel
from .learn_format_model import LearningFromatModel
from .student_work_model import StudentWorkModel


class CourseModel(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    type = Column(String)
    image_name = Column(String)
    practice = Column(Integer)
    home_work = Column(Integer)
    project_portfolio = Column(Integer)
    for_who_photo = Column(String)

    for_who = Column(Integer, ForeignKey('for_who.id'))
    start_group = Column(Integer, ForeignKey('start_group.id'))
    learn_format = Column(Integer, ForeignKey('learn_format.id'))
    student_work = Column(Integer, ForeignKey('student_work.id'))
    visible = Column(Boolean)

    for_who_rel = relationship(ForWhoModel, back_populates="course_rel")
    start_group_rel = relationship(StartGroupModel, back_populates="course_rel")
    learn_format_rel = relationship(LearningFromatModel, back_populates="course_rel")
    student_work_rel = relationship(StudentWorkModel, back_populates="course_rel")
