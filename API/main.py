from fastapi import FastAPI, HTTPException

# Run server: uvicorn main:app --reload

app = FastAPI()

# GET method defined in the localhost root
# The method invokes a function returning a string

@app.get("/")
async def root():
    return 'Hello FastAPI!'