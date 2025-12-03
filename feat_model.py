from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Feats(Base):
    __tablename__ = "Feats"

    Feat_ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Abillity_Req = Column(String)
    Level_Req = Column(Integer)
    Class_Req = Column(String)
    Race_Req = Column(String)
    Misc_Req = Column(String)
    Source = Column(String)
    Revised_Feat_ID = Column(Integer)