class Task:
    description = ""
    stages = []
    solution_method = None

    def __init__(self, condition):
        self.condition = condition
        answers = self.__class__.solution_method(condition)
        self.stages = [
            stage_class(solution) 
            for stage_class, solution 
            in zip(self.__class__.stages, answers)
        ]

    def get_items(self):
        
