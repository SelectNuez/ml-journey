from fastapi import FastAPI
from .schemas import Passenger
from .predict import predict_passenger

app = FastAPI()

@app.post("/predict")
def predict(passenger: Passenger):
    result = predict_passenger(passenger.model_dump())
    return {"prediction": result}
