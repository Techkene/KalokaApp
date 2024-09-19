from pydantic import ValidationError, UUID4
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import schemas.farm_data
import schemas.recommendation
import schemas.token
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import timedelta

import crud, schemas, models
from db.database import get_db
from core.auth import create_access_token, oauth2_scheme, ALGORITHM
from core.config import settings
from ai.genai_conn import askGPT

router = APIRouter()
auth_router = APIRouter()

@router.post("/", response_model=schemas.farmer.Farmer)
def create_farmer(farmer: schemas.farmer.FarmerCreate, db: Session = Depends(get_db)):
    db_farmer = crud.farmer.get_farmer_by_email(db, email=farmer.email)
    if db_farmer:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.farmer.create_farmer(db=db, farmer=farmer)

# def get_current_farmer(
#     db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
# ) -> models.Farmer:
#     try:
#         payload = jwt.decode(
#             token, settings.SECRET_KEY, algorithms=[ALGORITHM]
#         )
#         token_data = schemas.token.TokenPayload(**payload)
#     except (JWTError, ValidationError):
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Could not validate credentials",
#         )
#     farmer = crud.farmer.get_farmer(db, farmer_id=token_data.sub)
#     if not farmer:
#         raise HTTPException(status_code=404, detail="Farmer not found")
#     return farmer

# @auth_router.post("/login/me", response_model=schemas.farmer.Farmer)
# def test_token(current_user: schemas.farmer.Farmer = Depends(get_current_farmer)):
#     return current_user

# @router.post("/login", response_model=schemas.token.Token)
# def login_access_token(
#     db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
# ):
#     farmer = crud.farmer.authenticate_password(
#         db, username=form_data.username, password=form_data.password
#     )
#     if not farmer:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     return {
#         "access_token": create_access_token(
#             farmer.id, expires_delta=access_token_expires
#         ),
#         "token_type": "bearer",
#     }

# @router.post("/login/pin", response_model=schemas.token.Token)
# def login_pin(
#     *,
#     db: Session = Depends(get_db),
#     phone_number: str,
#     pin: str
# ):
#     farmer = crud.farmer.authenticate_pin(db, phone_number=phone_number, pin=pin)
#     if not farmer:
#         raise HTTPException(status_code=400, detail="Incorrect phone number or PIN")
#     elif not crud.farmer.is_active(farmer):
#         raise HTTPException(status_code=400, detail="Inactive user")
#     access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     return {
#         "access_token": create_access_token(
#             farmer.id, expires_delta=access_token_expires
#         ),
#         "token_type": "bearer",
#     }


# @auth_router.get("/{farmer_id}", response_model=schemas.farmer.Farmer)
# def read_farmer(farmer_id: UUID4, db: Session = Depends(get_db)):
#     db_farmer = get_current_farmer(db, farmer_id=farmer_id)
#     if db_farmer is None:
#         raise HTTPException(status_code=404, detail="Farmer not found")
#     return db_farmer

@router.get("/login", response_model=schemas.farmer.Farmer)
def read_farmer(farmer: schemas.farmer.FarmerLogin, db: Session = Depends(get_db)):
    db_farmer = crud.farmer.authenticate_password(db, username=farmer.username, password=farmer.password)
    if db_farmer is None:
        raise HTTPException(status_code=404, detail="Invalid Username or Password")
    return db_farmer

@router.put("/{farmer_id}", response_model=schemas.farmer.Farmer)
def update_farmer(farmer_id: int, farmer: schemas.farmer.FarmerUpdate, db: Session = Depends(get_db)):
    db_farmer = crud.farmer.update_farmer(db, farmer_id=farmer_id, farmer=farmer)
    if db_farmer is None:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return db_farmer

@router.delete("/{farmer_id}", response_model=schemas.farmer.Farmer)
def delete_farmer(farmer_id: int, db: Session = Depends(get_db)):
    db_farmer = crud.farmer.delete_farmer(db, farmer_id=farmer_id)
    if db_farmer is None:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return db_farmer

@router.post("/submit")
def trigger_api(farm_data: schemas.farm_data.FarmDataUse, db: Session = Depends(get_db)):
    retVal = askGPT(farm_data)
    return retVal
