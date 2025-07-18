from typing import List

from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

import models
from database import engine, sessionLocal

app = FastAPI()

models.BASE.metadata.create_all(bind=engine)


def get_db():
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()


class BikeCreate(BaseModel):  # for POST request with no ID
    name: str
    brand: str


class BikeResponse(BaseModel):  # for Response with ID
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
    db_bike = models.Bikes(name=bike.name, brand=bike.brand)
    db.add(db_bike)
    db.commit()
    db.refresh(db_bike)
    return db_bike


@app.put("/bikes/{bike_id}", response_model=BikeResponse)
def update_bike(bike_id: int, update_bike: BikeCreate, db: Session = Depends(get_db)):
    db_bike = db.query(models.Bikes).filter(models.Bikes.id == bike_id).first()
    if db_bike:
        db_bike.name = update_bike.name
        db_bike.brand = update_bike.brand
        db.commit()
        db.refresh(db_bike)
        return db_bike
    return {"error": "bike not found"}


@app.delete("/bikes/{bike_id}")
def delete_bike(bike_id: int, db: Session = Depends(get_db)):
    db_bike = db.query(models.Bikes).filter(models.Bikes.id == bike_id).first()
    if db_bike:
        db.delete(db_bike)
        db.commit()
        return {"message": "Bike deleted"}
    return {"error": "bike not found"}
