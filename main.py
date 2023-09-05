from fastapi import FastAPI
import functions as ft
import importlib

importlib.reload(ft)

# Run server: uvicorn main:app --reload

app = FastAPI()

# GET method defined in the localhost root
# The method invokes a function returning a string

# Pasar a Query

@app.get("/userdata")
async def userdata(user_id: str):
    return ft.userdata(user_id)

@app.get("/countreviews")
async def countreviews(startdate: str, endate:str):
    return ft.countreviews(startdate, endate)

@app.get("/genre")
async def genre(genre: str):
    return ft.genre(genre)

@app.get("/userforgenre")
async def userforgenre(genre: str):
    return ft.userforgenre(genre)

@app.get("/developer")
async def developer(dev: str):
    return ft.developer(dev)

@app.get("/game_recommendation")
async def game_recommendation(game_id: int):
    return ft.game_recommendation(game_id)