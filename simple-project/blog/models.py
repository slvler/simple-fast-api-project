from .database import Base

from sqlalchemy.orm import Mapped
from sqlalchemy import Column, Integer, String, Boolean

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True)
    title: Mapped[str] = Column(String)
    body: Mapped[str] = Column(String)
    content: Mapped[str] = Column(String)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.title!r}, fullname={self.body!r}), content={self.content!r}"


class Blog(Base):
    __tablename__ = "blogs"

    id: Mapped[int] = Column(Integer, primary_key=True)
    title: Mapped[str] = Column(String)
    content: Mapped[str] = Column(String)
    vote: Mapped[int] = Column(Integer)
    status: Mapped[bool] = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"Blog(id={self.id!r}, title={self.title!r}, content={self.content!r}), vote={self.vote!r}, status={self.status!r}"
