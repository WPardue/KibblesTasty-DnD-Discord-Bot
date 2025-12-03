from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Rules(Base):
    __tablename__ = "Rules"

    Rule_ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Rule_Text = Column(String)
    Source = Column(Integer)
    Revised_Rule_ID = Column(Integer)