from CGLib.algo.graham import graham
from base.task import Task
from base.taskstage import TaskStage
from base.taskitem import TaskItem


class GrahamItemInternalPoint(TaskItem):
    description = "Задана множина S із N точок на площині. Знайти внутрішню точку q."
    solution_method = graham
    max_mark = 0.25


class GrahamStageInternalPoint(TaskStage):
    description = "Задана множина S із N точок на площині. Знайти внутрішню точку q."
    items = [GrahamItemInternalPoint]


class GrahamItemOrderedList(TaskItem):
    description = "Використовуючи q як початок координат, побудувати упорядкований за полярним кутом список точок множини S, починаючи із точки \"початок\" проти годинникової стрілки."
    solution_method = graham
    max_mark = 0.25


class GrahamStageOrderedList(TaskStage):
    description = "Використовуючи q як початок координат, побудувати упорядкований за полярним кутом список точок множини S, починаючи із точки \"початок\" проти годинникової стрілки."
    items = []


class GrahamItemStartingPoint(TaskItem):
    description = "Знайти точку \"початок\"."
    solution_method = graham
    max_mark = 0.25
    

class GrahamStageStartingPoint(TaskStage):
    description = "Знайти точку \"початок\"."
    items = []


class GrahamItemPointTriplesLookup(TaskItem):
    description = "Починаючи з точки \"початок\", розглядаємо трійки сусідніх точок."
    solution_method = graham
    max_mark = 0.15


class GrahamItemAngleCheck(TaskItem):
    description = "Перевіряємо внутрішній кут по відношенню до q, який утворює трійка."
    solution_method = graham
    max_mark = 0.15


class GrahamItemAngleLessThanPi(TaskItem):
    description = "Якщо кут менше ПІ - просуваємось вперед по списку на точку (яка перевірялася на на крайність)."
    solution_method = graham
    max_mark = 0.25


class GrahamItemAngleIsPiOrGreater(TaskItem):
    description = "Якщо кут більше або дорівнює ПІ - вилучаємо середню точку трійки і повертаємось на точку назад по списку."
    solution_method = graham
    max_mark = 0.6


class GrahamItemStartingPointReached(TaskItem):
    description = "При досягненні точки \"початок\" третьою точкою трійки перевіряємо кут, якщо він менше ПІ, зупиняємося, інакше повертаємось на точку назад по списку."
    solution_method = graham
    max_mark = 0.1

class GrahamStageLookup(TaskStage):
    description = "Організувати обход."
    items = [
        GrahamItemPointTriplesLookup,
        GrahamItemAngleCheck,
        GrahamItemAngleLessThanPi,
        GrahamItemAngleIsPiOrGreater,
        GrahamItemStartingPointReached
    ]


class GrahamTask(Task):
    description = "Метод Грехема"
    stages = [
        GrahamStageInternalPoint,
        GrahamStageOrderedList,
        GrahamStageStartingPoint,
        GrahamStageLookup
    ]
