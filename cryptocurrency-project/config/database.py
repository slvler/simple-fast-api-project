from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_DATABASE_URL = "postgresql://user:password@db:5432/mydatabase"

# SQLAlchemy veritabanı motoru
engine = create_engine(SQL_DATABASE_URL, echo=True)

# Base sınıfı
Base = declarative_base()

# Tabloları oluştur
Base.metadata.create_all(bind=engine)

# Oturum ayarı
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)


