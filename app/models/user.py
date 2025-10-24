# User model - represents users in the database
# Fields to include:
# - id: primary key
# - username: unique username
# - email: unique email address
# - password_hash: hashed password (never store plain passwords!)
# - created_at: timestamp when user registered
# - updated_at: timestamp of last update
# Relationships:
# - blogs: one user can have many blogs
# - comments: one user can have many comments
# - likes: one user can like many blogs

# Example data structure:
# {
#     "id": 1,
#     "username": "john_doe",
#     "email": "john@example.com",
#     "password_hash": "$2b$12$hashed_password_here",
#     "created_at": "2025-01-15T10:30:00",
#     "updated_at": "2025-01-15T10:30:00"
# }