from fastapi import HTTPException
from fastapi.responses import JSONResponse
from schemas.saved_wallet_schemas import storeRequest, updateRequest
from sqlalchemy.orm import Session
from models.models import SavedWallet
from datetime import datetime

def index(db: Session):
    return db.query(SavedWallet).all()
def store(request: storeRequest, db: Session):
    saved_wallet_account = SavedWallet(
        name=request.name,
        address=request.address,
        asset_id=request.asset_id,
        network_id=request.network_id,
        type=request.type,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    try:
        db.add(saved_wallet_account)
        db.commit()
        db.refresh(saved_wallet_account)
        content = {"message": "Success"}
        return JSONResponse(content=content, status_code=200)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

def show(id: int, db: Session):
    savedWallet = db.query(SavedWallet).filter(SavedWallet.id == id).first()
    if not savedWallet:
        return {"message": "not found"}
    return savedWallet

def update(id: int, request: updateRequest, db: Session):
    savedWallet = db.query(SavedWallet).filter(SavedWallet.id == id)

    if not savedWallet.first():
        raise HTTPException(status_code=404, detail=f'{id} id not found')

    update_data = request.dict(exclude_unset=True)

    savedWallet.update(update_data)
    db.commit()
    return {"message": "success"}

def delete(id: int, db: Session):
    db.query(SavedWallet).filter(SavedWallet.id == id).delete(synchronize_session=False)
    db.commit()
    return {"message": "success"}