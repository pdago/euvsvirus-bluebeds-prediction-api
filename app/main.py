import json

from fastapi import FastAPI, Body, HTTPException

from pydantic import BaseModel
from starlette.requests import Request

from app.prediction_model import PredictionModel


class Api(FastAPI):
    def __init__(self):
        super(Api, self).__init__()

    def config(self, icu_stay_model: PredictionModel):
        self.icu_stay_model = icu_stay_model


app = Api()


@app.get("/")
async def root():
    return "The app is upp and running"

class Item(BaseModel):
    class Config:
        extra = "allow"

@app.put("/icu_stay_time")
async def predict_icu_stay_time(request: Item = Body(
    ...,
    example={
        "age": 49,
        "hypertension": 0,
        "cardiovascular_disease": 0,
        "diabetes": 0,
        "malignacy": 0,
        "cerebrovascular_disease": 0,
        "copd": 0,
        "chronic_kidney_disease": 0,
        "chronic_liver_disease": 0,
        "hiv_infection": 0,
        "fever": 1,
        "fatigue": 1,
        "dry_cough ": 1,
        "anorexia": 1,
        "myalgia": 1,
        "dyspnea": 0,
        "expectoration": 0,
        "pharyngalgia": 1,
        "diarrhea": 0,
        "nausea": 1,
        "dizziness": 0,
        "headache": 0,
        "vomiting": 0,
        "abdominal_pain": 0,
        "median_heart_rate": 87.1,
        "median_respiratory_rate": 18.75,
        "median_arterial_pressure": 90.17,
        "nr_of_preconditions": 0,
        "nr_of_symptoms": 7,
        "admission_type_icu_invasive": 0,
        "admission_type_icu_non_invasive": 0,
        "admission_type_non_icu": 1,
        "gender_female": 1,
        "gender_male": 0
    })):

    input_json = json.loads(request.json())

    missing_fields = [f for f in app.icu_stay_model.prediction_fields() if f not in input_json]
    if missing_fields:
        raise HTTPException(status_code=400, detail=f'Fields {",".join(missing_fields)} missing in the request')

    x = [input_json[f] for f in app.icu_stay_model.prediction_fields()]
    y = app.icu_stay_model.predict(x)
    return y


if __name__ == "main":
    from app.icu_stay_model import IcuStayModel
    model_path = "data/bed_duation_model_versus_virus_05APRIL2020.sav"
    prediction_fields = ["age", "hypertension", "cardiovascular_disease", "diabetes", "malignacy",
                         "cerebrovascular_disease", "copd", "chronic_kidney_disease", "chronic_liver_disease",
                         "hiv_infection", "fever", "fatigue", "dry_cough ", "anorexia", "myalgia", "dyspnea",
                         "expectoration", "pharyngalgia", "diarrhea", "nausea", "dizziness", "headache", "vomiting",
                         "abdominal_pain", "median_heart_rate", "median_respiratory_rate", "median_arterial_pressure",
                         "nr_of_preconditions", "nr_of_symptoms", "admission_type_icu_invasive",
                         "admission_type_icu_non_invasive", "admission_type_non_icu", "gender_female", "gender_male"]

    icu_stay_model = IcuStayModel(model_path, prediction_fields)
    app.config(icu_stay_model=icu_stay_model)
