from starlette.testclient import TestClient

from app.prediction_model import PredictionModel
from app.main import app

class MockPredictionModel(PredictionModel):
    def __init__(self, prediction_value):
        self.set_prediction_value(prediction_value)

    def set_prediction_value(self, prediction_value):
        self.prediction_value = prediction_value

    def predict(self, x):
        return self.prediction_value


client = TestClient(app)
model = MockPredictionModel(42)
app.config(icu_stay_model=model)


def test_returns_prediction_icu_stay_time():
    response = client.put("/icu_stay_time")
    assert response.status_code == 200

