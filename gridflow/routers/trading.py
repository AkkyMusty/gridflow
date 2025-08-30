from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from gridflow import models, schemas
from gridflow.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.TradeResponse)
def create_trade(trade: schemas.TradeCreate, db: Session = Depends(get_db)):
    # Optional: check users exist
    seller = db.query(models.User).filter(models.User.id == trade.seller_id).first()
    buyer = db.query(models.User).filter(models.User.id == trade.buyer_id).first()
    if not seller or not buyer:
        raise HTTPException(status_code=400, detail="Seller or Buyer not found")

    new_trade = models.Trade(**trade.dict())
    db.add(new_trade)
    db.commit()
    db.refresh(new_trade)
    return new_trade


@router.get("/", response_model=List[schemas.TradeResponse])
def list_trades(db: Session = Depends(get_db)):
    return db.query(models.Trade).all()


@router.get("/{trade_id}", response_model=schemas.TradeResponse)
def get_trade(trade_id: int, db: Session = Depends(get_db)):
    trade = db.query(models.Trade).filter(models.Trade.id == trade_id).first()
    if not trade:
        raise HTTPException(status_code=404, detail="Trade not found")
    return trade


@router.delete("/{trade_id}")
def delete_trade(trade_id: int, db: Session = Depends(get_db)):
    trade = db.query(models.Trade).filter(models.Trade.id == trade_id).first()
    if not trade:
        raise HTTPException(status_code=404, detail="Trade not found")
    db.delete(trade)
    db.commit()
    return {"detail": "Trade deleted successfully"}
