from .database import Model
from sqlalchemy import Column, String, Integer


class Sample(Model):
    __tablename__ = "sample"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
