import pytest

from app.icu_stay_model import IcuStayModel

MODEL_PATH = "app/data/bed_duation_model_versus_virus_05APRIL2020.sav"


def test_icu_stay_model():
    sample_x = [
        [49,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,0,1,0,0,0,0,87.1,18.75,90.17,0,7,0,0,1,1,0],
        [22,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,88.79,20.54,89.72,0,3,0,0,1,1,0],
        [51,1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,82.34,20.52,90.68,1,3,0,0,1,1,0],
        [44,1,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,0,0,0,84.63,19.24,91.87,1,5,0,0,1,0,1],
        [42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,87.35,20.51,93.3,0,0,0,1,0,0,1]]

    sample_y = [5, 5.0, 4.0, 6.0, 9.0]
    model = IcuStayModel(MODEL_PATH)

    for x, y in zip(sample_x, sample_y):
        assert y == pytest.approx(model.predict(x), abs=1.5)
