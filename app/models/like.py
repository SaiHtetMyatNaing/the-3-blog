# Like model - represents likes on blog posts
# Fields to include:
# - id: primary key
# - blog_id: foreign key to Blog (which blog is liked)
# - user_id: foreign key to User (who liked the blog)
# - created_at: timestamp when like was created
# Constraints:
# - Add unique constraint on (blog_id, user_id) so one user can only like a blog once
# Relationships:
# - blog: many likes belong to one blog
# - user: many likes belong to one user

# Example data structure:
# {
#     "id": 1,
#     "blog_id": 1,
#     "user_id": 5,
#     "created_at": "2025-01-15T10:30:00"
# }

# app/models/like.py
# This defines the Like table structure in the database

from sqlalchemy import Column, Integer, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Like(Base):
    """
    Like model - represents likes on blog posts.
    Users can like a blog post, but only once per blog.
    """
    
    # The table name in the database
    __tablename__ = "likes"
    
    # Primary key - unique identifier for each like
    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign key - which blog post is being liked
    blog_id = Column(Integer, ForeignKey("blogs.id"), nullable=False)
    
    # Foreign key - which user liked the blog
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Timestamp when the like was created
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # This constraint ensures a user can only like a blog once
    # If they try to like it again, the database will reject it
    __table_args__ = (
        UniqueConstraint('blog_id', 'user_id', name='unique_blog_user_like'),
    )
    
    # Relationships
    # Many likes belong to one blog
    blog = relationship("Blog", back_populates="likes")
    
    # Many likes belong to one user
    user = relationship("User", back_populates="likes")
    
    def __repr__(self):
        """String representation for debugging"""
        return f"<Like(id={self.id}, user_id={self.user_id}, blog_id={self.blog_id})>"