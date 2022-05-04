from unittest import TestCase
from CGLib.models.point import Point
from base.models.base import Region
from base.models.condition import PointListAndRegionCondition, PointListCondition
from base.models.graham import GrahamCenterPointCell, GrahamPiCompareCell, GrahamPoint, GrahamPointList, GrahamTable, GrahamTableRow, GrahamToAddCell, GrahamTrinityCell, PiCompare, ToAddGraham
from base.models.kd_tree import Intersection, KdTree, KdTreeInterscetionCell, KdTreeOrderedList, KdTreePartitionCell, KdTreePartitionTable, KdTreePartitionTableRow, KdTreePoint, KdTreePointCell, KdTreeSearchTable, KdTreeSearchTableRow, KdTreeToAddCell, Partition, ToAddKdTree
from tasks.graham import GrahamTask
from tasks.kd_tree import KdTreeTask


class TestTasks(TestCase):
    def test_graham(self):
        task = GrahamTask(PointListCondition(point_list=[
            Point(6,4),
            Point(4,2),
            Point(4,0),
            Point(1,0),
            Point(3,2),
            Point(2,4)
        ]))
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
                GrahamToAddCell(content=ToAddGraham.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[1], ordered.points[2], ordered.points[3])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[2]),
                GrahamToAddCell(content=ToAddGraham.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[2], ordered.points[3], ordered.points[4])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[3]),
                GrahamToAddCell(content=ToAddGraham.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[3], ordered.points[4], ordered.points[5])),
                GrahamPiCompareCell(content=PiCompare.more),
                GrahamCenterPointCell(content=ordered.points[4]),
                GrahamToAddCell(content=ToAddGraham.no)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[2], ordered.points[3], ordered.points[5])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[3]),
                GrahamToAddCell(content=ToAddGraham.yes)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[3], ordered.points[5], ordered.points[0])),
                GrahamPiCompareCell(content=PiCompare.more),
                GrahamCenterPointCell(content=ordered.points[5]),
                GrahamToAddCell(content=ToAddGraham.no)
            )),
            GrahamTableRow(cells=(
                GrahamTrinityCell(content=(ordered.points[2], ordered.points[3], ordered.points[0])),
                GrahamPiCompareCell(content=PiCompare.less),
                GrahamCenterPointCell(content=ordered.points[3]),
                GrahamToAddCell(content=ToAddGraham.yes)
            )),
        ])
        
        self.assertAlmostEqual(task.stages[0].items[0].answer, internal_point)
        self.assertEqual(task.stages[1].items[0].answer, ordered)
        self.assertEqual(task.stages[2].items[0].answer, origin)
        self.assertEqual(task.stages[3].items[0].answer, steps)

    def test_kd_tree(self):
        task = KdTreeTask(PointListAndRegionCondition(
            point_list=[
                Point(3, 2),
                Point(5, 1),
                Point(4, 3),
                Point(7, 3),
                Point(6, 2)
            ],
            region_x_range=(2, 5),
            region_y_range=(2, 4)
        ))
        ordered = KdTreeOrderedList(points=[
            KdTreePoint(x=3, y=2),
            KdTreePoint(x=4, y=3),
            KdTreePoint(x=5, y=1),
            KdTreePoint(x=6, y=2),
            KdTreePoint(x=7, y=3)
        ])
        partition_table = KdTreePartitionTable(rows=[
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=ordered.points[2]),
                KdTreePartitionCell(content=Partition.vertical)
            )),
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=ordered.points[1]),
                KdTreePartitionCell(content=Partition.horizontal)
            )),
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=ordered.points[0]),
                KdTreePartitionCell(content=Partition.vertical)
            )),
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=ordered.points[4]),
                KdTreePartitionCell(content=Partition.horizontal)
            )),
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=ordered.points[3]),
                KdTreePartitionCell(content=Partition.vertical)
            )),
        ])
        tree = KdTree(
            nodes=[
                ordered.points[2],
                ordered.points[1],
                ordered.points[0],
                ordered.points[4],
                ordered.points[3],
            ],
            region=Region(x_range=(2, 5), y_range=(2,4))
        )
        search_table = KdTreeSearchTable(rows=[
            KdTreeSearchTableRow(cells=(
                KdTreePointCell(content=ordered.points[2]),
                KdTreeToAddCell(content=ToAddKdTree.no),
                KdTreeInterscetionCell(content=Intersection.yes)
            )),
            KdTreeSearchTableRow(cells=(
                KdTreePointCell(content=ordered.points[1]),
                KdTreeToAddCell(content=ToAddKdTree.yes),
                KdTreeInterscetionCell(content=Intersection.yes)
            )),
            KdTreeSearchTableRow(cells=(
                KdTreePointCell(content=ordered.points[0]),
                KdTreeToAddCell(content=ToAddKdTree.yes),
                KdTreeInterscetionCell(content=Intersection.yes)
            ))
        ])

        self.assertEqual(task.stages[0].items[0].answer, ordered)
        self.assertEqual(task.stages[0].items[1].answer, partition_table)
        self.assertEqual(task.stages[1].items[0].answer, tree)
        self.assertEqual(task.stages[2].items[0].answer, search_table)
