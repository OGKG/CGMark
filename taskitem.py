class TaskItem:
    description = ""
    solution_method = None
    max_mark = 0


    def __init__(self, conditions):
        self.conditions = conditions

    def get_mark(self, inputs):
        pass
