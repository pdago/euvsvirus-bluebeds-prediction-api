import random

from starlette.testclient import TestClient

from app.prediction_model import PredictionModel
from app.main import app


class MockPredictionModel(PredictionModel):
    def __init__(self):
        self.set_prediction_value(42)

    def set_prediction_value(self, prediction_value):
        self.prediction_value = prediction_value

    def prediction_fields(self):
        return ["f1", "f2", "f3"]

    def predict(self, x):
        return self.prediction_value


client = TestClient(app)
model = MockPredictionModel()
app.config(icu_stay_model=model)


def test_returns_prediction_icu_stay_time():
    prediction_values = [random.randint(0, 999) for i in range(25)]
    for p in prediction_values:
        model.set_prediction_value(p)
        response = client.put("/icu_stay_time", json={"f1": 0, "f2": 1, "f3": 0})
        assert 200 == response.status_code
        assert p == int(response.text)


def test_returns_error_when_missing_field():
    model.set_prediction_value(42)
    response = client.put("/icu_stay_time", json={"f1": 0, "f2": 1})
    assert 400 == response.status_code
    assert {"detail": "Fields f3 missing in the request"} == response.json()
