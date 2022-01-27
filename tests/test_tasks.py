from unittest import TestCase
from CGLib.models.point import Point
from base.models.graham import GrahamCenterPointCell, GrahamPiCompareCell, GrahamPoint, GrahamPointList, GrahamTable, GrahamTableRow, GrahamToAddCell, GrahamTrinityCell, PiCompare, ToAdd
from builders.graham import GrahamModelBuilder
from tasks.graham import GrahamTask


class TestGrahamBuilder(TestCase):
    def test_init(self):
        task = GrahamTask([Point(6,4), Point(4,2), Point(4,0), Point(1,0), Point(3,2), Point(2,4)])
        internal_point = GrahamPoint(x=4.666666666666667, y=2.0)
        ordered = GrahamPointList(points=[
            GrahamPoint(x=1, y=0),
            GrahamPoint(x=4, y=0),
            GrahamPoint(x=6, y=4),
            GrahamPoint(x=2, y=4),
            GrahamPoint(x=4, y=2),
            GrahamPoint(x=3, y=2)
        ])
        origin = GrahamPoint(x=1, y=0)
        steps = GrahamTable(rows=[
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[0], ordered.points[1], ordered.points[2])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[1]),
                GrahamToAddCell(content=ToAdd.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[1], ordered.points[2], ordered.points[3])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[2]),
                GrahamToAddCell(content=ToAdd.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[2], ordered.points[3], ordered.points[4])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[3]),
                GrahamToAddCell(content=ToAdd.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[3], ordered.points[4], ordered.points[5])),
                GrahamPiCompareCell(content=PiCompare.more),
                GrahamCenterPointCell(content=ordered.points[4]),
                GrahamToAddCell(content=ToAdd.no)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[2], ordered.points[3], ordered.points[5])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[3]),
                GrahamToAddCell(content=ToAdd.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[3], ordered.points[5], ordered.points[0])),
                GrahamPiCompareCell(content=PiCompare.more),
                GrahamCenterPointCell(content=ordered.points[5]),
                GrahamToAddCell(content=ToAdd.no)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[2], ordered.points[3], ordered.points[0])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[3]),
                GrahamToAddCell(content=ToAdd.yes)
            )),
        ])
        
        self.assertAlmostEqual(task.stages[0].items[0].answer, internal_point)
        self.assertEqual(task.stages[1].items[0].answer, ordered)
        self.assertEqual(task.stages[2].items[0].answer, origin)
        self.assertEqual(task.stages[3].items[0].answer, steps)
