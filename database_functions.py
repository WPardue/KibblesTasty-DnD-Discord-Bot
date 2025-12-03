from feat_model import Base, Feats
from spell_model import Base, Spells
from spell_class_list_model import Base, Class_Spell_List
from class_model import Base, Class_Features
from feature_tag_model import Base, Feature_Tags
from rule_model import Base, Rules
from spell_tag_model import Base, Spell_Tags
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import or_

DATABASE_URL = "sqlite:///./D&D_Content_Database.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)


def GetFeatByName(name):
    session = Session()

    records = session.query(Feats).filter(Feats.Name.like(name)).all()
    session.close()
    return records

def GetSpellByName(name):
    session = Session()

    records = session.query(Spells).filter(Spells.Name.like(name)).all()
    session.close()
    return records

def GetRuleByName(name):
    session = Session()

    records = session.query(Rules).filter(Rules.Name.like(name)).all()
    session.close()
    return records

def GetClassFeatureByName(name):
    session = Session()

    records = session.query(Class_Features).filter(Class_Features.Name.like(name)).all()
    session.close()
    return records

def GetFeatRevision(name):
    session = Session()

    records = session.query(Feats).filter(Feats.Name.like(name)).all()

    record = session.query(Feats).filter(Feats.Name.like(name)).first()
    revised = session.query(Feats).filter(Feats.Revised_Feat_ID.like(record.Feat_ID))

    session.close()
    return record, revised