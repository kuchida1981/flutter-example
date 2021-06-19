from sqlalchemy import Column, Integer, String

from .database import Model


class Sample(Model):
    __tablename__ = "sample"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
