from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Spells(Base):
    __tablename__ = "Spells"

    Spell_ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Level = Column(Integer)
    School = Column(String)
    Cast_Time = Column(String)
    Range = Column(String)
    Duration = Column(String)
    Is_Concentration = Column(Boolean)
    Has_Somatic = Column(Boolean)
    Has_Verbal = Column(Boolean)
    Material_Consumed = Column(Boolean)
    Material_Cost = Column(Boolean)    
    Material_Description = Column(String)
    Description = Column(String)
    Source = Column(String)
    revised_spell_ID = Column(Integer)