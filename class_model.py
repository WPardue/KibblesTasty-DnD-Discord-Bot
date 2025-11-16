from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Class_Features(Base):
    __tablename__ = "Class_Features"

    Feature_ID = Column(Integer, primary_key=True)
    Class = Column(String)
    Subclass = Column(String)
    Name = Column(String)
    Level = Column(Integer)
    Description = Column(Integer)