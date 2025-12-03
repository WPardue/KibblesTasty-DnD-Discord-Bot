from fastapi import FastAPI
import database_functions


app = FastAPI()


@app.get("/spells/")
async def GetSpellAsync(name: str, revision: bool = False):
    if revision:
        return #CompareVersionsFunction
    else:
        return #GetSpellFunction

@app.get("/feats/")
async def GetFeatAsync(name: str, revision: bool = False):
    if revision:
        return #CompareVersionsFunction
    else:
        return #GetFeatFunction

@app.get("/rules/")
async def GetRulesAsync(name: str, revision: bool = False):
    if revision:
        return #CompareVersionsFunction
    else:
        return #GetRulesFunction

@app.get("/feature/")
async def GetFeatureAsync(name: str, revision: bool = False):
    if revision:
        return #CompareVersionsFunction
    else:
        return #GetFeatureFunction

@app.get("/list/spells")
async def GetSpellAsync(category: str):
    return #ContentList

@app.get("/list/feats")
async def GetSpellAsync(category: str):
    return #ContentList

@app.get("/list/rules")
async def GetSpellAsync(category: str):
    return #ContentList

@app.get("/list/class_features")
async def GetSpellAsync(category: str):
    return #ContentList