from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from gridflow import models, schemas
from gridflow.database import get_db

router = APIRouter()

# Create new energy reading
@router.post("/", response_model=schemas.EnergyReadingResponse)
def create_energy_reading(
    reading: schemas.EnergyReadingCreate, db: Session = Depends(get_db)
):
    new_reading = models.SmartMeterReading(**reading.dict())
    db.add(new_reading)
    db.commit()
    db.refresh(new_reading)
    return new_reading

# List all energy readings
@router.get("/", response_model=List[schemas.EnergyReadingResponse])
def list_energy_readings(db: Session = Depends(get_db)):
    return db.query(models.SmartMeterReading).all()

# Get a single reading by ID
@router.get("/{reading_id}", response_model=schemas.EnergyReadingResponse)
def get_energy_reading(reading_id: int, db: Session = Depends(get_db)):
    reading = db.query(models.SmartMeterReading).filter(models.SmartMeterReading.id == reading_id).first()
    if not reading:
        raise HTTPException(status_code=404, detail="Reading not found")
    return reading

# Delete a reading
@router.delete("/{reading_id}")
def delete_energy_reading(reading_id: int, db: Session = Depends(get_db)):
    reading = db.query(models.SmartMeterReading).filter(models.SmartMeterReading.id == reading_id).first()
    if not reading:
        raise HTTPException(status_code=404, detail="Reading not found")
    db.delete(reading)
    db.commit()
    return {"detail": "Reading deleted successfully"}
