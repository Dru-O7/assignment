from pydantic import BaseModel
import datetime

class QueryRequest(BaseModel):
    user_id: int
    query: str

class PurchaseRequest(BaseModel):
    user_id: int
    amount_inr: float

class PurchaseResponse(BaseModel):
    message: str
    transaction_id: int
    user_id: int
    gold_grams_purchased: float

class GoldPurchase(BaseModel):
    id: int
    user_id: int
    amount_inr: float
    gold_grams: float
    timestamp: datetime.datetime

    class Config:
        orm_mode = True