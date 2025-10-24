from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Database setup and configuration
#
# Components to create:
# 1. SQLAlchemy engine - connects to database
# 2. SessionLocal - database session factory
# 3. Base - declarative base class for models
# 4. get_db() - dependency function to get database session
#    - Yields database session
#    - Closes session after request is complete
#    - Use in FastAPI with Depends(get_db)
#
# 5. create_tables() - function to create all tables
#    - Calls Base.metadata.create_all(engine)
#    - Run this on application startup
#
# Import settings from config.py for DATABASE_URL


# Create database engine
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,  # Verify connections before using them
    pool_size=5,         # Connection pool size
    max_overflow=10      # Max connections beyond pool_size
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for models
Base = declarative_base()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()