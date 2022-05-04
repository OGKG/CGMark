from base.builder import ModelBuilder
from base.models.base import Point, Region
from base.models.kd_tree import Intersection, KdTree, KdTreeInterscetionCell, KdTreeOrderedList, KdTreePartitionCell, KdTreePartitionTableRow, KdTreePoint, KdTreePartitionTable, KdTreePointCell, KdTreeSearchTable, KdTreeSearchTableRow, KdTreeToAddCell, Partition, ToAddKdTree


class KdTreeModelBuilder(ModelBuilder):

    @classmethod
    def _build_methods(cls):
        return [
            cls._build_ordered_list,
            cls._build_partition_table,
            cls._build_tree,
            cls._build_search_table
        ]
    
    @staticmethod
    def _build_ordered_list(answer):
        return KdTreeOrderedList(points=[KdTreePoint(x=p.x, y=p.y) for p in answer])
    
    @staticmethod
    def _build_partition_table(answer):
        partition = lambda x: Partition.vertical if x else Partition.horizontal
        rows = [
            KdTreePartitionTableRow(cells=(
                KdTreePointCell(content=KdTreePoint(x=row[0].x, y=row[0].y)),
                KdTreePartitionCell(content=partition(row[1]))
            ))
            for row in answer
        ]

        return KdTreePartitionTable(rows=rows)
    
    @staticmethod
    def _build_tree(answer):
        return KdTree(
            nodes=[Point(x=p.x, y=p.y) for p in answer.nodes],
            region=Region(x_range=answer.x_range, y_range=answer.y_range)
        )
    
    @staticmethod
    def _build_search_table(answer):
        to_add = lambda x: ToAddKdTree.yes if x else ToAddKdTree.no
        intersection = lambda x: Intersection.yes if x else Intersection.no
        rows = [
            KdTreeSearchTableRow(cells=(
                KdTreePointCell(content=KdTreePoint(x=row[0].x, y=row[0].y)),
                KdTreeToAddCell(content=to_add(row[1])),
                KdTreeInterscetionCell(content=intersection(row[2]))
            ))
            for row in answer
        ]

        return KdTreeSearchTable(rows=rows)
