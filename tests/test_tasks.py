from unittest import TestCase
from base.task import Task
from base.taskstage import TaskStage
from base.taskitem import TaskItem
from CGLib.models import Point
from tasks.graham import GrahamTask


class TestTaskItem(TaskItem):
    max_mark = 1


class TestTaskStage(TaskStage):
    items = [TestTaskItem, TestTaskItem]


class TestTask(Task):
    stages = [TestTaskStage, TestTaskStage]
    solution_method = lambda x: (i for i in x)


class TestTasks(TestCase):
    def test_init(self):
        t = TestTask(i for i in range(4))
        self.assertEqual(t.stages[0].items[1].answer, 1)


class TestGrahamTask(TestCase):
    def test_init(self):
        task = GrahamTask([Point(6,4), Point(4,2), Point(4,0), Point(1,0), Point(3,2), Point(2,4)])
        
        internal_point = Point(4.666666666666667, 2.0)
        ordered = [Point(1, 0), Point(4, 0), Point(6, 4), Point(2, 4), Point(4, 2), Point(3, 2)]
        origin = Point(1, 0)
        steps = [
            ([ordered[0], ordered[1], ordered[2]], True),
            ([ordered[1], ordered[2], ordered[3]], True),
            ([ordered[2], ordered[3], ordered[4]], True),
            ([ordered[3], ordered[4], ordered[5]], False),
            ([ordered[2], ordered[3], ordered[5]], True),
            ([ordered[3], ordered[5], ordered[0]], False),
            ([ordered[2], ordered[3], ordered[0]], True)
        ]

        self.assertAlmostEqual(task.stages[0].items[0].answer, internal_point)
        self.assertEqual(task.stages[1].items[0].answer, ordered)
        self.assertEqual(task.stages[2].items[0].answer, origin)
        self.assertEqual(task.stages[3].items[0].answer, steps)
