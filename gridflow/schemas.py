from pydantic import BaseModel, EmailStr
from typing import Optional


# ---------- USER SCHEMAS ----------
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

from pydantic import BaseModel
from datetime import datetime

# --- Energy Reading ---
class EnergyReadingBase(BaseModel):
    meter_id: int
    energy_kwh: float

class EnergyReadingCreate(EnergyReadingBase):
    pass

class EnergyReadingResponse(EnergyReadingBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

