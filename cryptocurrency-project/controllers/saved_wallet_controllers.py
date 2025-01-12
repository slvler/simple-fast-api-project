from schemas.saved_wallet_schemas import storeRequest, updateRequest
from sqlalchemy.orm import Session

def index(db: Session):
    pass
def store(request: storeRequest, db: Session):
    pass
def show(id: int, db: Session):
    pass
def update(id: int, request: updateRequest, db: Session):
    pass
def delete(id: int, db: Session):
    pass