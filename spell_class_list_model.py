from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Class_Spell_List(Base):
    __tablename__ = "Class_Spell_List"

    Class = Column(String, primary_key=True)
    Spell_ID = Column(Integer, primary_key=True)