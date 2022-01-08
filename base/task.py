from typing import Any
from taskstage import TaskStage
from taskitem import TaskItem


class Task:
    description: str = ""
    stages: list[TaskStage] = []
    solution_method: function = None

    def __init__(self, condition: Any):
        self.condition = condition
        answers = self.__class__.solution_method(condition)
        self.stages = [
            stage_class(answers) 
            for stage_class
            in self.__class__.stages
        ]

    def get_items(self) -> list[TaskItem]:
        return [item for stage in self.stages for item in stage]
