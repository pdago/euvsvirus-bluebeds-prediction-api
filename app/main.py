from fastapi import FastAPI, Body

from api import prediction_model


class Api(FastAPI):
    def __init__(self):
        super(Api, self).__init__()

    def config(self, icu_stay_model: prediction_model):
        self.icu_stay_model = icu_stay_model


app = Api()


@app.get("/")
async def root():
    return "The app is upp and running"


@app.put("/icu_stay_time")
async def predict_icu_stay_time():
    y = app.icu_stay_model.predict(0)
    return y