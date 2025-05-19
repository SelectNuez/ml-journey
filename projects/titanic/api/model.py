import pickle
import os

def load_model():
    # Obtener ruta absoluta de este archivo (model.py)
    base_path = os.path.dirname(__file__)
    model_path = os.path.join(base_path, "..", "model.pkl")

    with open(model_path, "rb") as f:
        return pickle.load(f)
