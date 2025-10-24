# Comment Pydantic schemas - for request/response validation
#
# CommentCreate schema:
# - Fields: content, blog_id
# - user_id will come from authenticated user
# - Used when creating a new comment
#
# CommentUpdate schema:
# - Fields: content
# - Used when updating a comment
#
# CommentResponse schema:
# - Fields: id, content, blog_id, user_id, created_at, updated_at
# - Can include nested user info (username)
# - Used when returning comment data to client