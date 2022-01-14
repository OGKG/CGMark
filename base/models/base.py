from pydantic import BaseModel
from typing import Any, Iterable


class Point(BaseModel):
    x: float = 0
    y: float = 0


class PointList(BaseModel):
    points: list[Point] = []


class TableCell(BaseModel):
    content: Any


class TableRow(BaseModel):
    cells: Iterable[TableCell] = []


class Table(BaseModel):
    rows: Iterable[TableRow] = []
    

class HeaderTable(Table):
    headers = Iterable[str]
