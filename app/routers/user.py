from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_users():
    return {"message": "User router working"}

# User router - API endpoints for user operations
# 
# Endpoints to implement:
# 
# POST /users/register - Create a new user account
# Request body example:
# {
#     "username": "john_doe",
#     "email": "john@example.com",
#     "password": "myPassword123"
# }
# Response example:
# {
#     "id": 1,
#     "username": "john_doe",
#     "email": "john@example.com",
#     "created_at": "2025-01-15T10:30:00"
# }
#
# POST /users/login - Login and get authentication token
# Request body example:
# {
#     "email": "john@example.com",
#     "password": "myPassword123"
# }
# Response example:
# {
#     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
#     "token_type": "bearer"
# }
#
# GET /users/me - Get current authenticated user profile
# Requires: Authorization header with Bearer token
# Response example:
# {
#     "id": 1,
#     "username": "john_doe",
#     "email": "john@example.com",
#     "created_at": "2025-01-15T10:30:00"
# }
#
# GET /users/{user_id} - Get specific user profile by ID
# Response example: same as /users/me
#
# PUT /users/me - Update current user profile
# Requires: Authorization header with Bearer token
# Request body example:
# {
#     "username": "new_username",
#     "email": "newemail@example.com"
# }
#
# DELETE /users/me - Delete current user account
# Requires: Authorization header with Bearer token
#
# Remember to:
# - Hash passwords before storing (use bcrypt or passlib)
# - Generate JWT tokens for authentication
# - Protect endpoints that require authentication
# - Return appropriate HTTP status codes (200, 201, 400, 401, 404, etc.)