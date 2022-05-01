from pydantic import BaseModel
from CGLib.models import Graph, Point


class Condition(BaseModel):
    """Base task's condition model with CGLib-ish parameter types."""
    pass


class GraphAndPointCondition(Condition):
    graph: Graph
    point: Point

    class Config:
        arbitrary_types_allowed = True


class PointListCondition(Condition):
    point_list: list[Point]

    class Config:
        arbitrary_types_allowed = True


class PointListAndRegionCondition(PointListCondition):
    region_x_range: tuple[float, float] = (0.0, 0.0)
    region_y_range: tuple[float, float] = (0.0, 0.0)

    class Config:
        arbitrary_types_allowed = True
