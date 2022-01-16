from pydantic import BaseModel
from typing import Any


class Point(BaseModel):
    x: float = 0
    y: float = 0


class PointList(BaseModel):
    points: list[Point] = []


class TableCell(BaseModel):
    content: Any


class TableRow(BaseModel):
    cells: list[TableCell] = []


class Table(BaseModel):
    rows: list[TableRow] = []
    

class HeaderTable(Table):
    headers: list[str] = []
