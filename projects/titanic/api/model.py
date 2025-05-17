import pickle

def load_model():
    with open("projects/titanic/model.pkl", "rb") as f:
        return pickle.load(f)
