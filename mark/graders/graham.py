from mark.grader import Grader, default_grading
from mark.markdata import MarkData, StageMarkData, Mistake
from functools import partial

default025 = partial(default_grading, sub=0.25)
default125 = partial(default_grading, sub=1.25)



internal_point = StageMarkData(max_mark=0.25)
ordered = StageMarkData(max_mark=0.25)
origin = StageMarkData(max_mark=0.25)
steps_table = StageMarkData(max_mark=1.25)


class GrahamGrader(Grader):
    markdata = MarkData(stages=[internal_point, ordered, origin, steps_table])
    stage_grading_methods = [default025, default025, default025, default125]


