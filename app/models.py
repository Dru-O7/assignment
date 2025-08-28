from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    # Add other user details if needed, e.g., name, email

class GoldPurchase(Base):
    __tablename__ = "gold_purchases"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    amount_inr = Column(Float)
    gold_grams = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)