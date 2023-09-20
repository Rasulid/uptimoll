from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime, Time
from sqlalchemy.orm import relationship
from api.db.DataBase import Base


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
    visible = Column(Boolean)
    sub_title = Column(String)


    for_who_rel = relationship("ForWhoModel", back_populates="course")
    start_group_rel = relationship("StartGroupModel", back_populates="course")
    learn_format_rel = relationship("LearningFormatModel", back_populates="course")
    student_work_rel = relationship("StudentWorkModel", back_populates="course")


class ForWhoModel(Base):
    __tablename__ = 'for_who'
    # one-to-one relationship
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    course_id = Column(Integer, ForeignKey('course.id', ondelete="CASCADE"))

    course = relationship("CourseModel", back_populates="for_who_rel")


class StartGroupModel(Base):
    # many-to-one relationship
    __tablename__ = 'start_group'
    id = Column(Integer, primary_key=True, index=True)
    when_start = Column(String, nullable=False)
    group_lang = Column(String)
    time_start = Column(String)
    time_end = Column(String)
    weeks = Column(String)
    course_id = Column(Integer, ForeignKey("course.id", ondelete="CASCADE"))

    course = relationship("CourseModel", back_populates="start_group_rel")


class LearningFormatModel(Base):
    # many-to-one relationship
    __tablename__ = 'learn_format'
    id = Column(Integer, primary_key=True, index=True)
    group = Column(String)
    desc = Column(String)
    desc_2 = Column(String)
    price = Column(Integer)
    course_id = Column(Integer, ForeignKey("course.id", ondelete="CASCADE"))

    course = relationship("CourseModel", back_populates="learn_format_rel")


class StudentWorkModel(Base):
    # many-to-one relationship
    __tablename__ = 'student_work'
    id = Column(Integer, primary_key=True, index=True)
    link = Column(String)
    image_name = Column(String)
    visible = Column(Boolean)
    course_id = Column(Integer, ForeignKey('course.id', ondelete="CASCADE"))

    course = relationship("CourseModel", back_populates="student_work_rel")

