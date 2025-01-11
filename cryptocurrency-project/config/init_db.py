from sqlalchemy import create_engine
from database import Base

SQL_DATABASE_URL = "postgresql://user:password@db:5432/mydatabase"
engine = create_engine(SQL_DATABASE_URL)

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Veritabanı tabloları oluşturuldu!")

if __name__ == "__main__":
    init_db()
