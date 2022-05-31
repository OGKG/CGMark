from pydantic import BaseModel
from typing import Any


class Mistake(BaseModel):
    sub: float
    big_sub: float = 0
    data: Any

    @property
    def systematic(self):
        return self.big_sub > 0

    def __hash__(self):  # make hashable BaseModel subclass
        return hash((type(self),) + tuple(self.__dict__.values()))


class StageMarkData(BaseModel):
    max_mark: float
    min_mark: float = 0

    def __hash__(self):  # make hashable BaseModel subclass
        return hash((type(self),) + tuple(self.__dict__.values()))


class MarkData(BaseModel):
    stages: list[StageMarkData] = []
