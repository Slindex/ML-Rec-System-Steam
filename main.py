from fastapi import FastAPI, HTTPException
import functions as ft
import pandas as pd
import importlib

importlib.reload(ft)

# Run server: uvicorn main:app --reload

app = FastAPI()

# GET method defined in the localhost root
# The method invokes a function returning a string


@app.get("/userdata/{User_id}")
async def userdata(User_id: str):
    return ft.userdata(User_id)

@app.get("/countreviews")
async def countreviews(startdate: str, endate:str):
    return ft.countreviews(startdate, endate)

@app.get("/genre/{genre}")
async def genre(genre: str):
    return ft.genre(genre)