from pydantic import BaseModel
import pickle
import pandas as pd

with open("E:/porto/Website-Car Price Prediction/model/LRModel.pkl", "rb") as f:
    model = pickle.load(f)

class ScoringItem(BaseModel):
    Car_Name: str
    Year: int
    Present_Price: float
    Kms_Driven: int
    Fuel_Type: str
    Seller_Type: str
    Transmission: str
    Owner: int

async def scoring_endpoint(item: ScoringItem):
    print(item.dict())
    try:
        df = pd.DataFrame([item.dict()])
        print(df.head())  
        pred = model.predict(df)
        print(pred)  
    except Exception as e:
        return {"error": str(e)}  
        
    return f"Selling Price Prediction: {round(float(pred),2)}"
