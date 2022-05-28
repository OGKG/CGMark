from typing import Any


class TaskItem:
    description: str = ""
    data_model: None

    def __init__(self, answer: Any):
        self.answer = answer
