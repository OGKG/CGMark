from pydantic import BaseModel
from typing import Any


class Point(BaseModel):
    x: float = 0
    y: float = 0


class PointList(BaseModel):
    points: list[Point] = []


class Vertex(BaseModel):
    point: Point = None


class Edge(BaseModel):
    v1: Vertex = None
    v2: Vertex = None
    weight: int = 0


class Graph(BaseModel):
    vertices: set = set()
    edges: set = set()


class Region(BaseModel):
    x_range: tuple[int, int] = (0, 0)
    y_range: tuple[int, int] = (0, 0)


class TableCell(BaseModel):
    content: Any


class TableRow(BaseModel):
    cells: list[TableCell] = []


class Table(BaseModel):
    rows: list[TableRow] = []
    

class HeaderTable(Table):
    headers: list[str] = []
