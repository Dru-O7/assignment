from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user_id: int):
    db_user = models.User(id=user_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_gold_purchase(db: Session, purchase: schemas.PurchaseRequest, gold_grams: float):
    db_purchase = models.GoldPurchase(
        user_id=purchase.user_id,
        amount_inr=purchase.amount_inr,
        gold_grams=gold_grams
    )
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

def get_purchase_history(db: Session, user_id: int):
    return db.query(models.GoldPurchase).filter(models.GoldPurchase.user_id == user_id).all()