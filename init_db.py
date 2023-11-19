from database import engine,Base
from models import Category,Blog

Base.metadata.create_all(bind=engine)