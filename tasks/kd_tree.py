import base.models.kd_tree as models
from base.task import Task
from base.taskstage import TaskStage
from base.taskitem import TaskItem
from builders.kd_tree import KdTreeModelBuilder
from CGLib.algo.kd_tree_method import kd_tree
from CGLib.models.point import Point


class KdTreeItemOrderedList(TaskItem):
    description = "Побудувати відсортований по X список."
    solution_method = kd_tree
    max_mark = 0.25
    data_model = models.KdTreePoint


class KdTreeItemPartition(TaskItem):
    description = "Рекурсивно розбити площину на прямокутники."
    solution_method = kd_tree
    max_mark = 0.75
    data_model = models.KdTreePartitionTable


class KdTreeStagePreprocessing(TaskStage):
    description = "Попередня обробка"
    items = [KdTreeItemOrderedList, KdTreeItemPartition]


class KdTreeItemTree(TaskItem):
    description = "Побудувати дерево пошуку."
    solution_method = kd_tree
    max_mark = 1.0
    data_model = models.KdTree


class KdTreeStageTree(TaskStage):
    description = "Побудувати дерево пошуку."
    items = [KdTreeItemTree]


class KdTreeItemSearch(TaskItem):
    description = "Здійснити пошук у дереві."
    solution_method = kd_tree
    max_mark = 1.0
    data_model = models.KdTreeSearchTable


class KdTreeStageSearch(TaskStage):
    description = "Здійснити пошук у дереві."
    items = [KdTreeItemSearch]


class KdTreeTask(Task):
    item_answer_builder = KdTreeModelBuilder
    description = "Метод kd-дерева"
    stages = [
        KdTreeStagePreprocessing,
        KdTreeStageTree,
        KdTreeStageSearch
    ]
    solution_method = kd_tree

    @property
    def unwrapped_condition(self):
        return [
            [Point(p.x, p.y) for p in self.condition.point_list],
            self.condition.region_x_range,
            self.condition.region_y_range
        ]
