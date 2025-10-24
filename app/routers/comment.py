from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_comments():
    return {"message": "Comment router working"}

# Comment router - API endpoints for comment operations
#
# Endpoints to implement:
# POST /comments - Create a new comment on a blog (requires authentication)
# GET /comments/{comment_id} - Get a specific comment by ID
# PUT /comments/{comment_id} - Update a comment (only by comment author)
# DELETE /comments/{comment_id} - Delete a comment (by comment author or blog author)
#
# Note: Getting all comments for a blog should be in blog.py router
# GET /blogs/{blog_id}/comments
#
# Remember to:
# - Check if user is comment author before allowing updates
# - Allow blog author to delete comments on their blog
# - Verify blog exists before creating comment