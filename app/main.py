from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas, database
from .ai_service import process_query # Import the AI service

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "null", # For local file access
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

@app.post("/purchase_gold", response_model=schemas.PurchaseResponse)
def purchase_gold(request: schemas.PurchaseRequest, db: Session = Depends(database.get_db)):
    # Hardcoded gold price for simplicity (e.g., ₹7000/gram)
    GOLD_PRICE_PER_GRAM_INR = 7000.0

    gold_grams = request.amount_inr / GOLD_PRICE_PER_GRAM_INR

    # Ensure user exists or create a new one
    user = crud.get_user(db, user_id=request.user_id)
    if not user:
        user = crud.create_user(db, user_id=request.user_id)

    db_purchase = crud.create_gold_purchase(db, request, gold_grams)
    return schemas.PurchaseResponse(
        message="Gold purchased successfully!",
        transaction_id=db_purchase.id,
        user_id=db_purchase.user_id,
        gold_grams_purchased=db_purchase.gold_grams
    )

@app.post("/ask_kuberai")
async def ask_kuberai(request: schemas.QueryRequest):
    response_text, action = await process_query(request.query)
    return {"response": response_text, "action": action}

@app.get("/history/{user_id}", response_model=List[schemas.GoldPurchase])
def get_history(user_id: int, db: Session = Depends(database.get_db)):
    history = crud.get_purchase_history(db, user_id=user_id)
    return history