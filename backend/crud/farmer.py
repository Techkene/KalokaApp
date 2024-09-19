from sqlalchemy.orm import Session
from models.farmer import Farmer
from schemas.farmer import FarmerCreate, FarmerUpdate
from core.auth import verify_password, verify_pin, get_password_hash, get_pin_hash

def get_farmer(db: Session, farmer_id: int):
    return db.query(Farmer).filter(Farmer.id == farmer_id).first()

def get_farmer_by_email(db: Session, email: str):
    return db.query(Farmer).filter(Farmer.email == email).first()

def get_farmers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Farmer).offset(skip).limit(limit).all()

def get_farmer_by_username(db: Session, username: str):
    return db.query(Farmer).filter(Farmer.username == username).first()

def get_farmer_by_phone(db: Session, phone_number: str):
    return db.query(Farmer).filter(Farmer.phone_number == phone_number).first()

def create_farmer(db: Session, farmer: FarmerCreate):
    hashed_password = get_password_hash(farmer.password)
    hashed_pin = get_pin_hash(farmer.pin)
    db_farmer = Farmer(
        email=farmer.email,
        hashed_password=hashed_password,
        username=farmer.username,
        is_independent=farmer.is_independent,
        hashed_pin=hashed_pin,
        phone_number=farmer.phone_number
        )
    db.add(db_farmer)
    db.commit()
    db.refresh(db_farmer)
    return db_farmer

def update_farmer(db: Session, farmer_id: int, farmer: FarmerUpdate):
    db_farmer = get_farmer(db, farmer_id)
    if db_farmer:
        update_data = farmer.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_farmer, key, value)
        db.add(db_farmer)
        db.commit()
        db.refresh(db_farmer)
    return db_farmer

def delete_farmer(db: Session, farmer_id: int):
    farmer = get_farmer(db, farmer_id)
    if farmer:
        db.delete(farmer)
        db.commit()
    return farmer

def authenticate_password(db: Session, username: str, password: str):
    farmer = get_farmer_by_username(db, username=username)
    if not farmer:
        return None
    if not verify_password(password, farmer.hashed_password):
        return None
    return farmer

def authenticate_pin(db: Session, phone_number: str, pin: str):
    farmer = get_farmer_by_phone(db, phone_number=phone_number)
    if not farmer:
        return None
    if not verify_pin(pin, farmer.hashed_pin):
        return None
    return farmer
