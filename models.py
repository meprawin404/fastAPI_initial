from sqlalchemy import Column, Integer, String

from database import BASE


class Bikes(BASE):
    __tablename__ = "bikes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    brand = Column(String)
