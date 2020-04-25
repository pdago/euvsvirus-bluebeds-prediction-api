from abc import ABC


class PredictionModel(ABC):
    def predict(self, x):
        pass

    def prediction_fields(self):
        pass
