from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Spell_Tags(Base):
    __tablename__ = "Spell_Tags"

    Tag = Column(String, primary_key=True)
    Spell_ID = Column(Integer, primary_key=True)