from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from run_wmd import calculate

items = []

def search (item_id):
    for item in items:
        if item.id == item_id:
            return item

class Item(BaseModel):
    id: int
    title: str
    description: str | None = None

app = FastAPI()

origins = [
    "http://localhost:*",
    "http://localhost:3000",
    "http://localhost:3000/",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Items": len(items)}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return search(item_id)

@app.post("/items/{item.id}")
async def create_item(item: Item):
    items.append(item)
    result = calculate(item.title, item.description, item.id)
    return result