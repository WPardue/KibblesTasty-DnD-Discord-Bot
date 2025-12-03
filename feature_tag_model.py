from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Feature_Tags(Base):
    __tablename__ = "Feature_Tags"

    Tag = Column(String, primary_key=True)
    Feature_ID = Column(Integer, primary_key=True)