from backend_v2.code.app.db.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey, Column
from sqlalchemy.orm import relationship
from uuid import uuid4


class Admin_model(Base):
    __tablename__ = "admins"
    id = Column(String, primary_key=True, default=str(uuid4()), unique=True)
    username = Column(String, unique=True)
    password = Column(String)
    is_superuser = Column(Boolean, default=False)
    is_stuff = Column(Boolean, default=True)


