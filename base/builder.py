from base.task import Task


class ModelBuilder:
    def __init__(self, task: Task):
        self.task = task
    
    @property
    def _build_methods(self):
        pass

    def build(self):
        k = 0
        for i, stage in enumerate(self.task.stages):
            for j, item in enumerate(stage.items):
                self.task.stages[i].items[j].answer = self._build_methods[k](item.answer)
                k += 1
