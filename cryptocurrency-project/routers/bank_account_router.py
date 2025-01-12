from fastapi import APIRouter, Depends
from schemas.bank_account_schemas import storeRequest, updateRequest
from config.database import SessionLocal
from sqlalchemy.orm import Session
from controllers.bank_account_controllers import index, store, show, update, delete

bank_router = APIRouter(prefix='/bank-account', tags=['bank_account'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@bank_router.get("/")
def index_request(db: Session = Depends(get_db)):
    return index(db)

@bank_router.post("/store")
def store_request(request: storeRequest, db: Session = Depends(get_db)):
    return store(request, db)

@bank_router.get("/{id}")
def show_request(id: int, db: Session = Depends(get_db)):
    return show(id, db)

@bank_router.put("/{id}")
def update_request(id: int, request: updateRequest, db: Session = Depends(get_db)):
    return update(id, request, db)

@bank_router.delete("/{id}")
def delete_request(id: int, db: Session = Depends(get_db)):
    return delete(id, db)
