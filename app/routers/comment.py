from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_comments():
    return {"message": "Comment router working"}

# Comment router - API endpoints for comment operations
#
# Endpoints to implement:
# 
# POST /comments - Create a new comment on a blog (requires authentication)
# Requires: Authorization header with Bearer token
# Request body example:
# {
#     "content": "Great blog post!",
#     "blog_id": 1
# }
# Response example:
# {
#     "id": 1,
#     "content": "Great blog post!",
#     "blog_id": 1,
#     "user_id": 5,
#     "username": "john_doe",
#     "created_at": "2025-01-15T10:30:00"
# }
#
# GET /comments/{comment_id} - Get a specific comment by ID
# Response example: single comment with user info
#
# PUT /comments/{comment_id} - Update a comment (only by comment author)
# Requires: Authorization header with Bearer token
# Request body example:
# {
#     "content": "Updated comment text"
# }
#
# DELETE /comments/{comment_id} - Delete a comment (by comment author or blog author)
# Requires: Authorization header with Bearer token
#
# Note: Getting all comments for a blog should be in blog.py router
# GET /blogs/{blog_id}/comments
#
# Remember to:
# - Check if user is comment author before allowing updates
# - Allow blog author to delete comments on their blog
# - Verify blog exists before creating comment