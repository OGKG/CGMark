from base.models.graham import GrahamTable
from mark.grader import Grader, default_grading, iterable_grading
from mark.markdata import MarkData, StageMarkData, Mistake
from functools import partial


default025 = partial(default_grading, sub=0.25)
iterable025 = partial(iterable_grading, sub=0.25)


def steps_table_grading(correct: GrahamTable, answer: GrahamTable):
    """"
    row.cells[0] - points' triple
    row.cells[1] - less/more than pi (True/False)
    row.cells[2] - center point
    row.cells[3] - add/delete the point (True/False)
    """
    mistakes = []
    correct_triples = [row.cells[0] for row in correct.rows]
    answer_triples = [row.cells[0] for row in answer.rows]
    correct_angles = [row.cells[1] for row in correct.rows]
    answer_angles = [row.cells[1] for row in correct.rows]
    correct_less_than_pi = [
        (row.cells[1], row.cells[3], correct.rows[i+1].cells[0])
        for i, row in enumerate(correct.rows[:-1])
        if row.cells[1]
    ]
    answer_less_than_pi = [
        (row.cells[1], row.cells[3], correct.rows[i+1].cells[0])
        for i, row in enumerate(correct.rows[:-1])
        if row.cells[1]
    ]
    correct_more_than_pi = [
        (row.cells[1], row.cells[3], correct.rows[i+1].cells[0])
        for i, row in enumerate(correct.rows[:-1])
        if not row.cells[1]
    ]
    answer_more_than_pi = [
        (row.cells[1], row.cells[3], correct.rows[i+1].cells[0])
        for i, row in enumerate(correct.rows[:-1])
        if not row.cells[1]
    ]
    mistakes_last = [
        Mistake(sub=0.25)
        for row in answer.rows
        if row.cells[0].content[1] == answer.rows[0].cells[0].content[0]
    ] + ([Mistake(sub=0.25)] if answer.rows[-1] != correct.rows[-1] else [])

    mistakes.extend(iterable_grading(correct_triples, answer_triples, sub=0.15))
    mistakes.extend(iterable_grading(correct_angles, answer_angles, sub=0.15))
    mistakes.extend(iterable_grading(correct_less_than_pi, answer_less_than_pi, sub=0.25))
    mistakes.extend(iterable_grading(correct_more_than_pi, answer_more_than_pi, sub=0.3, cum_sub=0.6))
    mistakes.extend(mistakes_last)

    return mistakes


internal_point = StageMarkData(max_mark=0.25)
ordered = StageMarkData(max_mark=0.25)
origin = StageMarkData(max_mark=0.25)
steps_table = StageMarkData(max_mark=1.25)


class GrahamGrader(Grader):
    markdata = MarkData(stages=[internal_point, ordered, origin, steps_table])
    stage_grading_methods = [default025, iterable025, default025, steps_table_grading]
