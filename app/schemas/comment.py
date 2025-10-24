# Comment Pydantic schemas - for request/response validation
#
# CommentCreate schema - When someone comments on a blog:
# Fields: content, blog_id
# user_id will come from authenticated user
# Used when creating a new comment
# Example:
# {
#     "content": "Great blog post!",
#     "blog_id": 1
# }
#
# CommentUpdate schema - When editing their comment:
# Fields: content
# Used when updating a comment
# Example:
# {
#     "content": "Updated comment text"
# }
#
# CommentResponse schema - Comment details:
# Fields: id, content, blog_id, user_id, created_at, updated_at
# Can include nested user info (username)
# Used when returning comment data to client
# Example:
# {
#     "id": 1,
#     "content": "Great blog post!",
#     "blog_id": 1,
#     "user_id": 5,
#     "username": "john_doe",
#     "created_at": "2025-01-15T10:30:00",
#     "updated_at": "2025-01-15T11:00:00"
# }
#
# Validation rules:
# - content: minimum 1 character, required