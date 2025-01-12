from schemas.bank_account_schemas import storeRequest, updateRequest
from models.models import BankAccount
from datetime import datetime
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

def index(db: Session):
    return db.query(BankAccount).all()

def store(request: storeRequest, db: Session):
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


def show(id: int, db: Session):
    bankAccount = db.query(BankAccount).filter(BankAccount.id == id).first()
    if not bankAccount:
        return {"message": "not found"}
    return bankAccount


def update(id: int, request: updateRequest, db: Session):
    bankAccount = db.query(BankAccount).filter(BankAccount.id == id)

    if not bankAccount.first():
        raise HTTPException(status_code=404, detail=f'{id} id not found')

    update_data = request.dict(exclude_unset=True)

    bankAccount.update(update_data)
    db.commit()
    return {"message": "success"}

def delete(id: int, db: Session):
    db.query(BankAccount).filter(BankAccount.id == id).delete(synchronize_session=False)
    db.commit()
    return {"message": "success"}