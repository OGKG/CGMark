from base.task import Task
from base.taskstage import TaskStage
from base.taskitem import TaskItem
from unittest import TestCase


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