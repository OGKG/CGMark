from typing import Any, Callable
from base import TaskStage
from base import TaskItem


class Task:
    description: str = ""
    stages: list[TaskStage] = []
    solution_method: Callable = None
    item_answer_builder = None

    def __init__(self, condition: Any):
        self.condition = condition
        raw_answers = self.__class__.solution_method(condition)
        answers = self.item_answer_builder.build(raw_answers)
        self.stages = [
            stage_class(answers) 
            for stage_class
            in self.__class__.stages
        ]

    def get_items(self) -> list[TaskItem]:
        return [item for stage in self.stages for item in stage.items]
