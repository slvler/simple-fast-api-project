from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP


from database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(Text)
    is_active = Column(Boolean, default=False)
    slug = Column(String(50), unique=True)
    blogs = relationship('Blog', back_populates='category_relation')

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(Text)
    is_active = Column(Boolean, default=False)
    slug = Column(String(50), unique=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category_relation = relationship('Category', back_populates='blogs')


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))
