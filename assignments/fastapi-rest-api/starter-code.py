# Starter code for FastAPI REST API assignment

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Example data model
class Item(BaseModel):
    id: int
    name: str
    description: str = ""

items: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}

# Add CRUD endpoints below
# Example:
# @app.post("/items/")
# def create_item(item: Item):
#     ...

# You can run this server with: uvicorn starter-code:app --reload
