from pydantic import BaseModel

class Passenger(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    Fare: float
    SibSp: int
    Parch: int
    Embarked: str
    Title: str  