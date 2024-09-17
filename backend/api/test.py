from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core import security
from app.core.config import settings

router = APIRouter()

@router.post("/login/access-token", response_model=schemas.Token)
def login_access_token(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    farmer = crud.farmer.authenticate_password(
        db, username=form_data.username, password=form_data.password
    )
    if not farmer:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    elif not crud.farmer.is_active(farmer):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            farmer.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }

@router.post("/login/pin", response_model=schemas.Token)
def login_pin(
    *,
    db: Session = Depends(deps.get_db),
    phone_number: str,
    pin: str
):
    """
    PIN-based login for WhatsApp/SMS, get an access token for future requests
    """
    farmer = crud.farmer.authenticate_pin(db, phone_number=phone_number, pin=pin)
    if not farmer:
        raise HTTPException(status_code=400, detail="Incorrect phone number or PIN")
    elif not crud.farmer.is_active(farmer):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            farmer.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }

@router.post("/login/test-token", response_model=schemas.Farmer)
def test_token(current_user: schemas.Farmer = Depends(deps.get_current_user)):
    """
    Test access token
    """
    return current_user