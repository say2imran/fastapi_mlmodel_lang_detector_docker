from os.path import abspath
from os.path import join
from os.path import dirname
import os, sys
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
sys.path.append(abspath(join(dirname(__file__), '..')))
from ml_model.model import predict_pipeline
from ml_model.model import __version__ as model_version


app = FastAPI()


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
