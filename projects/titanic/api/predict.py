import pandas as pd
from .model import load_model

model = load_model()

def predict_passenger(passenger_data: dict) -> int:
    df = pd.DataFrame([passenger_data])
    prediction = model.predict(df)[0]
    return int(prediction)
