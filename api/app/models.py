from typing import List

from pydantic import BaseModel


class Sample(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class SampleIn(BaseModel):
    name: str

    class Config:
        orm_mode = True


SampleList = List[Sample]


class PaginationParams:
    def __init__(self, limit: int = 10, offset: int = 0):
        self.limit = limit
        self.offset = offset
