from fastapi.testclient import TestClient
from projects.titanic.api.main import app


client = TestClient(app)

def test_predict_survivor():
    payload = {
        "Pclass": 1,
        "Sex": 1,
        "Age": 30.0,
        "Fare": 100.0
    }
    
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] in [0,1]
    
def test_predict_error():
    payload = {
        "Pclass": 3,
        "Sex": 999,
        "Age": "MyAge",
        "Fare": -50
    }
    
    
    response = client.post("/predict", json=payload)
    print(response)
    assert response.status_code != 200


