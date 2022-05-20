from pydantic import BaseModel
from base.models.base import Point, Graph


class Condition(BaseModel):
    pass


class GraphAndPointCondition(Condition):
    graph: Graph
    point: Point


class PointListCondition(Condition):
    point_list: list[Point]


class PointListAndRegionCondition(PointListCondition):
    region_x_range: tuple[float, float] = (0.0, 0.0)
    region_y_range: tuple[float, float] = (0.0, 0.0)
