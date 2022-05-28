from typing import Any


class TaskItem:
    description: str = ""

    def __init__(self, answer: Any):
        self.answer = answer
