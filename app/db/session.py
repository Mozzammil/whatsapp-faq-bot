from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Create engine
engine = create_engine(settings.DATABASE_URL)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()