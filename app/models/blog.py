# Blog model - represents blog posts in the database
# Fields to include:
# - id: primary key
# - title: blog post title
# - content: blog post content/body
# - author_id: foreign key to User (who wrote this blog)
# - category_id: foreign key to Category (optional)
# - created_at: timestamp when blog was created
# - updated_at: timestamp of last update
# - is_published: boolean to track if blog is published
# Relationships:
# - author: many blogs belong to one user
# - category: many blogs can belong to one category
# - comments: one blog can have many comments
# - likes: one blog can have many likes

# Example data structure:
# {
#     "id": 1,
#     "title": "My First Blog Post",
#     "content": "This is my amazing blog content...",
#     "author_id": 5,
#     "category_id": 1,
#     "is_published": true,
#     "created_at": "2025-01-15T10:30:00",
#     "updated_at": "2025-01-15T14:20:00"
# }

# app/models/blog.py
# This defines the Blog table structure in the database

from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Blog(Base):
    """
    Blog model - represents blog posts in the database.
    Each blog is written by a user and can belong to a category.
    """
    
    # The table name in the database
    __tablename__ = "blogs"
    
    # Primary key - unique identifier for each blog post
    id = Column(Integer, primary_key=True, index=True)
    
    # The title of the blog post
    title = Column(String, nullable=False, index=True)
    
    # The main content/body of the blog post
    content = Column(Text, nullable=False)
    
    # Foreign key - links to the User who wrote this blog
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Foreign key - links to the Category this blog belongs to (optional)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    
    # Whether the blog is published or still a draft
    is_published = Column(Boolean, default=True)
    
    # Timestamp when the blog was created
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Timestamp of last update
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    # Many blogs belong to one user (author)
    author = relationship("User", back_populates="blogs")
    
    # Many blogs can belong to one category
    category = relationship("Category", back_populates="blogs")
    
    # One blog can have many comments
    comments = relationship("Comment", back_populates="blog", cascade="all, delete-orphan")
    
    # One blog can have many likes
    likes = relationship("Like", back_populates="blog", cascade="all, delete-orphan")
    
    def __repr__(self):
        """String representation for debugging"""
        return f"<Blog(id={self.id}, title={self.title})>"