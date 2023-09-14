from typing import Union
import asyncio
import json
import os
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from run_wmd import calculate

items = []

def getModels ():
    folder = f"{os.getcwd()}/model"
    files = os.listdir(folder)
    return files

def search (item_id):
    for item in items:
        if item.id == item_id:
            return item

class Item(BaseModel):
    id: int
    title: str
    description: str | None = None
    model: str

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

@app.get("/models")
def read_root():
    return getModels()


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return search(item_id)

@app.post("/items/{item.id}")
async def create_item(item: Item):
    items.append(item)
    return calculate(item.title, item.description, item.id, item.model)