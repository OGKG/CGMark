from functools import partial
from base.models.quickhull import QuickhullPartition, QuickhullTree
from mark.grader import Grader, default_grading, iterable_grading
from mark.markdata import MarkData, StageMarkData


default025 = partial(default_grading, sub=0.25)
iterable025 = partial(iterable_grading, sub=0.25)
iterable1 = partial(iterable_grading, sub=1.0)


def grade_partition(correct: QuickhullPartition, answer: QuickhullPartition):
    mistakes = []
    correct_extreme_points = correct.initial_partition.min_point, correct.initial_partition.max_point
    answer_extreme_points = answer.initial_partition.min_point, answer.initial_partition.max_point
    
    correct_h_points = [node.data.h for node in correct.tree.nodes if node.data.h is not None]
    answer_h_points = [node.data.h for node in answer.tree.nodes if node.data.h is not None]
    
    correct_points = [
        (
            node.data.points,
            node.left.points if node.left else None,
            node.right.points if node.right else None
        )
        for node in correct.tree.nodes
    ]
    answer_points = [
        (
            node.data.points,
            node.left.points if node.left else None,
            node.right.points if node.left else None
        )
        for node in answer.tree.nodes
    ]

    mistakes.extend(default025(correct_extreme_points, answer_extreme_points))
    mistakes.extend(iterable025(correct_h_points, answer_h_points, cum_sub=0.5))
    mistakes.extend(iterable025(correct_points, answer_points))
    mistakes.extend(iterable025(correct.tree.leaves, answer.tree.leaves))


def grade_merge(correct: QuickhullTree, answer: QuickhullTree):
    return iterable1(
        [node.data.hull_piece for node in correct.nodes],
        [node.data.hull_piece for node in answer.nodes]
    )


partition = StageMarkData(max_mark=1.0)
merge = StageMarkData(max_mark=1.0)


class QuickhullGrader(Grader):
    markdata = MarkData(stages=[partition, merge])
    stage_grading_methods = [grade_partition, grade_merge]
