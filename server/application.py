from fastapi import FastAPI
from pydantic import BaseModel
from API.scoring import scoring_endpoint, ScoringItem

app = FastAPI()

class ScoringItem(BaseModel):
    Car_Name: str
    Year: int
    Present_Price: float
    Kms_Driven: int
    Fuel_Type: str
    Seller_Type: str
    Transmission: str
    Owner: int

@app.post('/')
async def predict(item: ScoringItem):
    return await scoring_endpoint(item)
