from pydantic import BaseModel
from datetime import date

class TrainModel(BaseModel):
    product_name: str

class PredictRequest(BaseModel):
    days: int
    product_name: str

class Sale(BaseModel):
    order_date: date = date.today()
    product_name: str
    quantity: int