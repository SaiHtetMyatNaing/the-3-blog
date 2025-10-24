# User Pydantic schemas - for request/response validation
# 
# UserCreate schema - When someone registers (signs up):
# Fields: username, email, password
# Used when creating a new user (registration)
# Example:
# {
#     "username": "john_doe",
#     "email": "john@example.com",
#     "password": "myPassword123"
# }
#
# UserLogin schema - When someone logs in:
# Fields: email, password
# Used for user login
# Example:
# {
#     "email": "john@example.com",
#     "password": "myPassword123"
# }
#
# UserResponse schema - What we send back (NO PASSWORD!):
# Fields: id, username, email, created_at
# DO NOT include password_hash in responses!
# Used when returning user data to client
# Example:
# {
#     "id": 1,
#     "username": "john_doe",
#     "email": "john@example.com",
#     "created_at": "2025-01-15T10:30:00"
# }
#
# UserUpdate schema - When they want to change their profile:
# Fields: username (optional), email (optional)
# Used when updating user profile
# Example:
# {
#     "username": "new_username",
#     "email": "newemail@example.com"
# }
#
# Validation rules:
# - username: 3-50 characters, alphanumeric with _ and -
# - email: must be valid email format
# - password: minimum 8 characters