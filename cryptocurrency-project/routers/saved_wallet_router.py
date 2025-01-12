from fastapi import APIRouter, Depends
from schemas.saved_wallet_schemas import storeRequest, updateRequest
from config.database import SessionLocal
from sqlalchemy.orm import Session
from controllers.saved_wallet_controllers import index, store, show, update, delete
from middlewares.saved_wallet_midd import router_middleware

saved_wallet = APIRouter(prefix='/saved-wallet', tags=['saved_wallet'])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@saved_wallet.get("/")
def index_request(db: Session = Depends(get_db)):
    return index(db)
@saved_wallet.post("/store")
def store_request(request: storeRequest, db: Session = Depends(get_db), auth: bool = Depends(router_middleware)):
    return store(request, db)
@saved_wallet.get("/{id}")
def show_request(id: int, db: Session = Depends(get_db)):
    return show(id, db)
@saved_wallet.put("/{id}")
def update_request(id: int, request: updateRequest, db: Session = Depends(get_db)):
    return update(id, request, db)
@saved_wallet.delete("/{id}")
def delete_request(id: int, db: Session = Depends(get_db)):
    return delete(id, db)