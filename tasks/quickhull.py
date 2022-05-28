from CGLib.algo.quickhull import quickhull
from base.models import quickhull as models
from base.taskitem import TaskItem


class QuickhullItemInitialPartition(TaskItem):
    description = "Знайти точки min(x) та max(x) і розділити множину S із N точок на дві підмножини."
    solution_method = quickhull


class QuickhullItemPartition(TaskItem):
    description = "Здійснити подальше розбиття."
    solution_method = quickhull
