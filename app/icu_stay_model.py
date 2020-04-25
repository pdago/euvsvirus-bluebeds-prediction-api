import numpy as np

from app.prediction_model import PredictionModel
import joblib
from loguru import logger

class IcuStayModel(PredictionModel):
    def __init__(self, model_path, fields=None):
        self._model = joblib.load(model_path)
        self._fields = fields

    def predict(self, x):
        prediction = self._model.predict(np.expand_dims(np.array(x), 0))
        return float(prediction)

    def prediction_fields(self):
        return self._fields
