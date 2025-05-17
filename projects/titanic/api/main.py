from fastapi import FastAPI
from projects.titanic.api.shemas import Passenger
from projects.titanic.api.predict import predict_passenger

app = FastAPI()

@app.post("/predict")
def predict(passenger: Passenger):
    result = predict_passenger(passenger.dict())
    return {"prediction": result}
