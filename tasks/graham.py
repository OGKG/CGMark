import base.models.graham as models
from CGLib.algo.graham import graham
from base.task import Task
from base.taskstage import TaskStage
from base.taskitem import TaskItem


class GrahamItemInternalPoint(TaskItem):
    description = "Задана множина S із N точок на площині. Знайти внутрішню точку q."
    solution_method = graham
    max_mark = 0.25
    data_model = models.GrahamPoint


class GrahamStageInternalPoint(TaskStage):
    description = "Задана множина S із N точок на площині. Знайти внутрішню точку q."
    items = [GrahamItemInternalPoint]


class GrahamItemOrderedList(TaskItem):
    description = "Використовуючи q як початок координат, побудувати упорядкований за полярним кутом список точок множини S, починаючи із точки \"початок\" проти годинникової стрілки."
    solution_method = graham
    max_mark = 0.25
    data_model = models.GrahamPointList


class GrahamStageOrderedList(TaskStage):
    description = "Використовуючи q як початок координат, побудувати упорядкований за полярним кутом список точок множини S, починаючи із точки \"початок\" проти годинникової стрілки."
    items = [GrahamItemOrderedList]


class GrahamItemStartingPoint(TaskItem):
    description = "Знайти точку \"початок\"."
    solution_method = graham
    max_mark = 0.25
    data_model = models.GrahamPoint    

class GrahamStageStartingPoint(TaskStage):
    description = "Знайти точку \"початок\"."
    items = [GrahamItemStartingPoint]


class GrahamItemLookup(TaskItem):
    description = "Організувати обхід."
    solution_method = graham
    data_model = models.GrahamTable


class GrahamStageLookup(TaskStage):
    description = "Організувати обхід."
    items = [GrahamItemLookup]


class GrahamTask(Task):
    description = "Метод Грехема"
    stages = [
        GrahamStageInternalPoint,
        GrahamStageOrderedList,
        GrahamStageStartingPoint,
        GrahamStageLookup
    ]
