# User Pydantic schemas - for request/response validation
# 
# UserCreate schema:
# - Fields: username, email, password
# - Used when creating a new user (registration)
#
# UserLogin schema:
# - Fields: email, password
# - Used for user login
#
# UserResponse schema:
# - Fields: id, username, email, created_at
# - DO NOT include password_hash in responses!
# - Used when returning user data to client
#
# UserUpdate schema:
# - Fields: username (optional), email (optional)
# - Used when updating user profile