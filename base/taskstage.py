class TaskStage:
    description: str = ""
    items: "list[TaskItem]" = []

    def __init__(staged_answers) -> None:
        self.items = [item_class(answer) for item_class, answer in zip(self.__cls__.items, staged_answers)]