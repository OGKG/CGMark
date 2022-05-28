from base.models import graham as models
from base.task import Task
from base.taskstage import TaskStage
from base.taskitem import TaskItem
from builders.graham import GrahamModelBuilder
from CGLib.algo.graham import graham
from CGLib.models.point import Point


class GrahamItemInternalPoint(TaskItem):
    description = "Задана множина S із N точок на площині. Знайти внутрішню точку q."


class GrahamStageInternalPoint(TaskStage):
    description = "Задана множина S із N точок на площині. Знайти внутрішню точку q."
    items = [GrahamItemInternalPoint]


class GrahamItemOrderedList(TaskItem):
    description = "Використовуючи q як початок координат, побудувати упорядкований за полярним кутом список точок множини S, починаючи із точки \"початок\" проти годинникової стрілки."


class GrahamStageOrderedList(TaskStage):
    description = "Використовуючи q як початок координат, побудувати упорядкований за полярним кутом список точок множини S, починаючи із точки \"початок\" проти годинникової стрілки."
    items = [GrahamItemOrderedList]


class GrahamItemOriginPoint(TaskItem):
    description = "Знайти точку \"початок\"."


class GrahamStageOriginPoint(TaskStage):
    description = "Знайти точку \"початок\"."
    items = [GrahamItemOriginPoint]


class GrahamItemLookup(TaskItem):
    description = "Організувати обхід."


class GrahamStageLookup(TaskStage):
    description = "Організувати обхід."
    items = [GrahamItemLookup]


class GrahamTask(Task):
    item_answer_builder = GrahamModelBuilder
    description = "Метод Грехема"
    stages = [
        GrahamStageInternalPoint,
        GrahamStageOrderedList,
        GrahamStageOriginPoint,
        GrahamStageLookup
    ]
    solution_method = graham

    @property
    def unwrapped_condition(self):
        return [[Point(p.x, p.y) for p in self.condition.point_list]]
