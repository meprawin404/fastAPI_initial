from typing import List

from fastapi import FastAPI, Depends
from pydantic import BaseModel

import models
from database import engine, sessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.BASE.metadata.create_all(bind = engine)

def get_db():
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()


class Bike(BaseModel):
    name: str
    brand: str


bikes: List[Bike] = []


@app.get("/")
def read_root():
    return {"msg": "welcome to Bikers"}


@app.get("/bikes")
def get_bikes():
    return bikes


@app.post("/bikes")
def add_bikes(bike: Bike):
    bikes.append(bike)
    return bike


@app.put("/bikes/{bike_id}")
def update_bike(bike_id: int, updated_bike: Bike):
    for index, bike in enumerate(bikes):
        if bike.id == bike_id:
            bikes[index] = updated_bike
            return updated_bike

    return {"error": "bike not find"}


@app.delete("/bikes/{bike_id}")
def delete_bike(bike_id):
    for index, bike in enumerate(bikes):
        if bike.id == bike_id:
            data = bikes.pop(index)
            return data

    return {"error": "bike not found"}
