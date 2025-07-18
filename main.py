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


class BikeCreate(BaseModel): #for POST request with no ID
    name: str
    brand: str

class BikeResponse(BaseModel): #for Response with ID
    id: int
    name: str
    brand: str

    class Config:
        from_attributes = True  


# bikes: List[Bike] = []


@app.get("/")
def read_root():
    return {"msg": "welcome to Bikers"}


@app.get("/bikes", response_model=List[BikeResponse])
def get_bikes(db: Session = Depends(get_db)):
    return db.query(models.Bikes).all()


@app.post("/bikes", response_model=BikeResponse)
def add_bikes(bike: BikeCreate, db: Session = Depends(get_db)):
    db_bike = models.Bikes(name = bike.name, brand = bike.brand)
    db.add(db_bike)
    db.commit()
    db.refresh(db_bike)
    return db_bike


