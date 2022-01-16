from base import Point, HeaderTable, TableCell, TableRow, PointList
from enum import Enum, auto


class GrahamPoint(Point):
    pass


class GrahamPointList(PointList):
    pass


class GrahamTrinityCell(TableCell):
    content: tuple[Point, Point, Point]


class PiCompare(Enum):
    less = auto()
    more = auto()


class GrahamPiCompareCell(TableCell):
    content: PiCompare


class GrahamCenterPointCell(TableCell):
    content: Point


class ToAdd(Enum):
    yes: auto()
    no: auto()


class GrahamToAddCell(TableCell):
    content: ToAdd


class GrahamTableRow(TableRow):
    cells: tuple[GrahamTrinityCell, GrahamPiCompareCell, GrahamCenterPointCell, GrahamToAddCell]


class GrahamTable(HeaderTable):
    rows: list[GrahamTableRow]
    headers: tuple[str, str, str, str] = ('', '', '', '')
