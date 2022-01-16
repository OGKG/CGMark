from typing import Any


class TaskItem:
    description: str = ""
    max_mark: float = 0
    data_model: None


    def __init__(self, answer: Any):
        self.answer = answer
