from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from api.db.DataBase import Base


class LearningFromatModel(Base):
    __tablename__ = 'learn_format'
    id = Column(Integer, primary_key=True, index=True)
    group = Column(String)
    desc = Column(String)
    desc_2 = Column(String)
    price = Column(Integer)
    course_id = Column(Integer, ForeignKey("course.id", ondelete="CASCADE"))

    course_rel = relationship('CourseModel', back_populates="learn_format_rel")
