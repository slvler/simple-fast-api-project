from config.database import Base

from sqlalchemy.orm import Mapped
from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime
from enums.general_status import Status
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String)
    email: Mapped[str] = Column(String)
    password: Mapped[str] = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r}), password={self.password!r}"

class BankAccount(Base):
    __tablename__ = "bank_accounts"

    id = Column(Integer, primary_key=True)
    currency_id: Mapped[int] = Column(Integer)
    label: Mapped[str] = Column(String)
    iban: Mapped[str] = Column(String)
    bank_name: Mapped[str] = Column(String)
    bank_account: Mapped[str] = Column(String)
    swift_number: Mapped[str] = Column(String)
    type = Column(
        Enum(Status, name="general_status_enum"),
        nullable=False
    )
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SavedWallet(Base):
    __tablename__ = "saved_wallets"

    id = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String)
    address: Mapped[str] = Column(String)
    asset_id: Mapped[int] = Column(Integer)
    network_id: Mapped[int] = Column(Integer)
    type = Column(
        Enum(Status, name="general_status_enum"),
        nullable=False
    )
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)