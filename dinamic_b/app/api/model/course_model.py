from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import BaseModel


class CourseModel(BaseModel):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)
    title_ru = Column(String)

    description = Column(String)
    description_ru = Column(String)

    type = Column(String)
    type_ru = Column(String)

    image_name = Column(String)

    practice = Column(Integer)

    home_work = Column(Integer)

    project_portfolio = Column(Integer)

    visible = Column(Boolean)

    sub_title = Column(String)
    sub_title_ru = Column(String)

    for_who_rel = relationship("ForWhoModel", back_populates="course")
    start_group_rel = relationship("StartGroupModel", back_populates="course")
    learn_format_rel = relationship("LearningFormatModel", back_populates="course")
    student_work_rel = relationship("StudentWorkModel", back_populates="course")


class ForWhoModel(BaseModel):
    __tablename__ = 'for_who'

    # one-to-one relationship
    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)
    title_ru = Column(String)

    description = Column(String)
    description_ru = Column(String)

    course_id = Column(Integer, ForeignKey('course.id', ondelete="SET NULL"))

    course = relationship("CourseModel", back_populates="for_who_rel")


class StartGroupModel(BaseModel):
    # many-to-one relationship
    __tablename__ = 'start_group'

    id = Column(Integer, primary_key=True, index=True)

    when_start = Column(String, nullable=False)
    when_start_ru = Column(String, nullable=False)

    group_lang = Column(String)
    group_lang_ru = Column(String)

    time_start = Column(String)
    time_start_ru = Column(String)

    time_end = Column(String)
    time_end_ru = Column(String)

    weeks = Column(String)
    weeks_ru = Column(String)

    course_id = Column(Integer, ForeignKey("course.id", ondelete="SET NULL"))

    course = relationship("CourseModel", back_populates="start_group_rel")


class LearningFormatModel(BaseModel):
    # many-to-one relationship
    __tablename__ = 'learn_format'

    id = Column(Integer, primary_key=True, index=True)

    group = Column(String)
    group_ru = Column(String)

    desc = Column(String)
    desc_ru = Column(String)

    desc_2 = Column(String)
    desc_2_ru = Column(String)

    price = Column(String)

    course_id = Column(Integer, ForeignKey("course.id", ondelete="SET NULL"))

    course = relationship("CourseModel", back_populates="learn_format_rel")


class StudentWorkModel(BaseModel):
    # many-to-one relationship
    __tablename__ = 'student_work'

    id = Column(Integer, primary_key=True, index=True)
    link = Column(String)
    image_name = Column(String)
    visible = Column(Boolean)

    course_id = Column(Integer, ForeignKey('course.id', ondelete="SET NULL"))

    course = relationship("CourseModel", back_populates="student_work_rel")
