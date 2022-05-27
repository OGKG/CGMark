from unittest import TestCase
from base.models.base import Point, PointList
from base.models.graham import GrahamCenterPointCell, GrahamPiCompareCell, GrahamTable, GrahamTableRow, GrahamToAddCell, GrahamTrinityCell, PiCompare, ToAddGraham
from mark.graders.graham import GrahamGrader, StageMarkData


class TestGraders(TestCase):
    def test_graham_grader(self):
        centroid = Point(x=3.3333333333333335, y=1.0)
        ordered = PointList(points=[Point(x=7, y=0), Point(x=3, y=3), Point(x=0, y=0)])
        origin = Point(x=7, y=0)
        steps_table = GrahamTable(rows=[
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[0], ordered.points[1], ordered.points[2])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[1]),
                GrahamToAddCell(content=ToAddGraham.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[1], ordered.points[2], ordered.points[0])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[1]),
                GrahamToAddCell(content=ToAddGraham.yes)
            ))
        ])
        answer_steps_table = GrahamTable(rows=[
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[0], ordered.points[1], ordered.points[2])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[1]),
                GrahamToAddCell(content=ToAddGraham.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[1], ordered.points[2], ordered.points[0])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[1]),
                GrahamToAddCell(content=ToAddGraham.no)
            ))
        ])

        correct = [
            centroid,
            ordered,
            origin,
            steps_table
        ]
        answer = [
            centroid,
            ordered,
            origin,
            answer_steps_table
        ]
        mark = GrahamGrader.grade(correct, answer)
        self.assertEqual(mark[0], 1.75)
        markdata = [
            (StageMarkData(max_mark=0.25, min_mark=0), 0.25), 
            (StageMarkData(max_mark=0.25, min_mark=0), 0.25), 
            (StageMarkData(max_mark=0.25, min_mark=0), 0.25), 
            (StageMarkData(max_mark=1.25, min_mark=0), 1.0)
        ]
        self.assertEqual(mark[1], markdata)


