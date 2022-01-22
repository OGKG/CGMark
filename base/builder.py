from base.task import Task


class ModelBuilder:
    def __init__(self, task: Task):
        self.task = task
    
    @property
    def _build_methods(self):
        pass

    def build(self) -> None:
        pairs = zip(self._build_methods, self.task.get_items())
        data_model_answers = [build_item(item.answer) for build_item, item in pairs]
        for item, new_answer in zip(self.task.get_items(), data_model_answers):
            item.answer = new_answer
