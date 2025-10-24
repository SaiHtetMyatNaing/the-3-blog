# Category model - represents blog categories in the database
# Fields to include:
# - id: primary key
# - name: category name (unique)
# - description: category description (optional)
# - created_at: timestamp when category was created
# Relationships:
# - blogs: one category can have many blogs

# Example data structure:
# {
#     "id": 1,
#     "name": "Technology",
#     "description": "All about tech stuff",
#     "created_at": "2025-01-15T10:30:00"
# }

# app/models/category.py
# This defines the Category table structure in the database

from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Category(Base):
    """
    Category model - represents blog categories in the database.
    Categories help organize blogs by topic (e.g., Technology, Travel, Food)
    """
    
    # The table name in the database
    __tablename__ = "categories"
    
    # Primary key - unique identifier for each category
    id = Column(Integer, primary_key=True, index=True)
    
    # Category name - must be unique (e.g., "Technology")
    name = Column(String, unique=True, nullable=False, index=True)
    
    # Optional description of what the category is about
    description = Column(Text, nullable=True)
    
    # Timestamp when the category was created
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    # One category can have many blogs
    blogs = relationship("Blog", back_populates="category")
    
    def __repr__(self):
        """String representation for debugging"""
        return f"<Category(id={self.id}, name={self.name})>"