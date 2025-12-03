from typing import Optional
from pydantic import BaseModel

class Feat(BaseModel):
    Feat_ID: int
    Name: str
    Abillity_Req: str
    Level_Req: int
    Class_Req: str
    Race_Req: str
    Misc_Req: str
    Source: str
    Revised_Feat_ID: int