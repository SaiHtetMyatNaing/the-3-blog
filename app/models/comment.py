# Comment model - represents comments on blog posts
# Fields to include:
# - id: primary key
# - content: comment text
# - blog_id: foreign key to Blog (which blog this comment is on)
# - user_id: foreign key to User (who wrote this comment)
# - created_at: timestamp when comment was created
# - updated_at: timestamp of last update
# Relationships:
# - blog: many comments belong to one blog
# - user: many comments belong to one user

# Example data structure:
# {
#     "id": 1,
#     "content": "Great blog post!",
#     "blog_id": 1,
#     "user_id": 5,
#     "created_at": "2025-01-15T10:30:00",
#     "updated_at": "2025-01-15T10:30:00"
# }

# app/models/comment.py
# This defines the Comment table structure in the database

from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Comment(Base):
    """
    Comment model - represents comments on blog posts.
    Users can write comments on any blog post.
    """
    
    # The table name in the database
    __tablename__ = "comments"
    
    # Primary key - unique identifier for each comment
    id = Column(Integer, primary_key=True, index=True)
    
    # The comment text/content
    content = Column(Text, nullable=False)
    
    # Foreign key - which blog post this comment is on
    blog_id = Column(Integer, ForeignKey("blogs.id"), nullable=False)
    
    # Foreign key - which user wrote this comment
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Timestamp when the comment was created
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Timestamp of last update
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    # Many comments belong to one blog
    blog = relationship("Blog", back_populates="comments")
    
    # Many comments belong to one user
    user = relationship("User", back_populates="comments")
    
    def __repr__(self):
        """String representation for debugging"""
        return f"<Comment(id={self.id}, user_id={self.user_id}, blog_id={self.blog_id})>"