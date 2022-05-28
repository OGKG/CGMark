from CGLib.algo.quickhull import quickhull
from CGLib.models.point import Point
from base.models import quickhull as models
from base.task import Task
from base.taskitem import TaskItem
from base.taskstage import TaskStage
from builders.quickhull import QuickhullModelBuilder


class QuickhullItemPartition(TaskItem):
    description = "Здійснити розбиття. Подати у вигляді дерева."


class QuickhullStagePartition(TaskStage):
    description = "Здійснити розбиття. Подати у вигляді дерева."
    items = [QuickhullItemPartition]


class QuickhullItemMerge(TaskItem):
    description = "Злиття. Рекурсивний підйом, результат - конкатенація списків. Починаючи із листків дерева, рекурсивно конкатенуємо упорядковані за годинниковою стрілкою списки."


class QuickhullStageMerge(TaskStage):
    description = "Злиття. Рекурсивний підйом, результат - конкатенація списків. Починаючи із листків дерева, рекурсивно конкатенуємо упорядковані за годинниковою стрілкою списки."
    items = [QuickhullItemMerge]


class QuickhullTask(Task):
    item_answer_builder = QuickhullModelBuilder
    description = "Метод Швидкобол"
    stages = [QuickhullStagePartition, QuickhullStageMerge]
    solution_method = quickhull

    @property
    def unwrapped_condition(self):
        return [[Point(p.x, p.y) for p in self.condition.point_list]]
