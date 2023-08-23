from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from api.db.DataBase import Base


class ForWhoModel(Base):
    __tablename__ = 'for_who'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    sub_title = Column(String)
    description = Column(String)
    course_id = Column(Integer, ForeignKey('course.id', ondelete="CASCADE"), nullable=False)

    course_rel = relationship('CourseModel', back_populates="for_who_rel")
