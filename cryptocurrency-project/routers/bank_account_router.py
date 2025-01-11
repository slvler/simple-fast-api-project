from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from schemas.bank_account_schemas import storeRequest
from models.models import BankAccount
from config.database import SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime

bank_router = APIRouter(prefix='/bank-account', tags=['bank_account'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@bank_router.post("/store")
def register(request: storeRequest, db: Session = Depends(get_db)):

    new_bank_account = BankAccount(
        currency_id=request.currency_id,
        label=request.label,
        iban=request.iban,
        bank_name=request.bank_name,
        bank_account=request.bank_account,
        swift_number=request.swift_number,
        type=request.type,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    try:
        db.add(new_bank_account)
        db.commit()
        db.refresh(new_bank_account)
        content = {"message": "Success"}
        return JSONResponse(content=content, status_code=200)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

