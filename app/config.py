from pydantic_settings import BaseSettings
from typing import Optional

# Configuration settings for the application
# 
# Settings to include:
# - DATABASE_URL: connection string for database (SQLite, PostgreSQL, etc.)
# - SECRET_KEY: secret key for JWT token generation
# - ALGORITHM: algorithm for JWT (usually "HS256")
# - ACCESS_TOKEN_EXPIRE_MINUTES: how long tokens are valid
# - API_V1_PREFIX: API version prefix (e.g., "/api/v1")
# - PROJECT_NAME: name of the project
# - DEBUG: debug mode flag
#
# Use pydantic BaseSettings to load from environment variables
# This allows configuration through .env file
# Never commit sensitive data like SECRET_KEY to git!

class Settings(BaseSettings):
    # Database - NeonDB PostgreSQL
    database_url: str = "postgresql://user:password@host/dbname"
    # Get this from your NeonDB dashboard
    
    # JWT Settings
    secret_key: str = "your-secret-key-change-this-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # App Settings
    app_name: str = "The Idiots Blog API"
    debug: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()