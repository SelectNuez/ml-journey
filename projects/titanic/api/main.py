from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

# ----------- MODELO (entrenado previamente) -----------
# Carga el modelo entrenado
with open("projects/titanic/api/model.pkl", "rb") as f:
    model = pickle.load(f)

# ----------- FASTAPI SETUP -----------
app = FastAPI()

# ----------- SCHEMA DE ENTRADA -----------
class Passenger(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    Fare: float

# ----------- ENDPOINT DE PREDICCIÓN -----------
@app.post("/predict")
def predict(passenger: Passenger):
    input_data = pd.DataFrame([passenger.model_dump()])
    prediction = model.predict(input_data)[0]
    return {"prediction": int(prediction)}
