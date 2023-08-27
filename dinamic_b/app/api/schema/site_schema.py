from typing import List

from pydantic import BaseModel

from api.schema.course_schema import CourseReadSchema
from api.schema.for_who_schema import ForWhoSiteSchema
from api.schema.learning_format_schema import LearningFormatSiteSchema
from api.schema.student_work_schema import StudentWorkSiteSchema
from api.schema.start_group_schema import StartGroupSiteSchema


class SiteSchema(BaseModel):
    course: CourseReadSchema
    for_who: List[ForWhoSiteSchema]
    start_group: List[StartGroupSiteSchema]
    learning_format: List[LearningFormatSiteSchema]
    student_work: List[StudentWorkSiteSchema]

    class Config:
        orm_mode = True
