from lib2to3.pytree import Base
from pydantic import BaseModel
from typing import Any


class Mistake(BaseModel):
    sub: float
    data: Any
    cumulative: bool = True

    def __hash__(self):  # make hashable BaseModel subclass
        return hash((type(self),) + tuple(self.__dict__.values()))


class StageMarkData(BaseModel):
    max_mark: float
    min_mark: float = 0

    def __hash__(self):  # make hashable BaseModel subclass
        return hash((type(self),) + tuple(self.__dict__.values()))


class MarkData(BaseModel):
    stages: list[StageMarkData] = []