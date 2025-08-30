import threading
from typing import List, Tuple
from baigel.model_control.infer_result import InferTracker, ModelTracker
from baigel.model_control.model_base import ModelBase
from baigel.models.dit_base import DitBaseModel
from baigel.models.dit_large import DitLargeModel
# from baigel.models.donut_docvqa import DonutDocvqaModel
from baigel.models.donut_to_data import DonutToDataModel
from baigel.models.donut_to_text import DonutToTextModel
from baigel.models.qag_en_base import QagEnBaseModel
from baigel.models.qnli_en_base import QnliEnBaseModel
from baigel.models.qa_en_large import QaEnLargeModel
from baigel.models.qa_en_base import QaEnBaseModel


class Models(object):
    def __init__(self, model_classes: List[type(ModelBase)]):
        self.model_classes = {model.id: model for model in model_classes}
        self.model_instances = {}
        self.lock = threading.Lock()

    def list(self) -> List[type(ModelBase)]:
        return [m for m in self.model_classes.values()]

    def has(self, model_id) -> type(ModelBase):
        return model_id in self.model_classes

    def get_type(self, model_id) -> type(ModelBase):
        if not self.has(model_id):
            raise ValueError(f'can not get type for unknown model {model_id}')
        return self.model_classes[model_id]

    def get(self, model_id: str) -> ModelBase:
        if model_id not in self.model_instances:
            self.model_instances[model_id] = self.get_type(model_id)()
        return self.model_instances[model_id]

    def get_tracked(self, model_id: str, infer_res: InferTracker) -> Tuple[ModelBase, ModelTracker]:
        tracker = infer_res.tracker(model_id)
        if model_id not in self.model_instances:
            with self.lock:
                if model_id not in self.model_instances:
                    on_loaded = tracker('load')
                    self.model_instances[model_id] = self.get_type(model_id)()
                    on_loaded()
        return self.model_instances[model_id], tracker


models = Models([
    DitBaseModel,
    DitLargeModel,
    # DonutDocvqaModel,
    DonutToDataModel,
    DonutToTextModel,
    QaEnBaseModel,
    QaEnLargeModel,
    QagEnBaseModel,
    QnliEnBaseModel,
])
