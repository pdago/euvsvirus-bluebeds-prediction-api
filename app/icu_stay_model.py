from app.prediction_model import PredictionModel


class IcuStayModel(PredictionModel):
    def __init__(self):
        pass

    def predict(self, x):
        return 42
