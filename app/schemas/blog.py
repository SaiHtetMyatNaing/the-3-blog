# Blog Pydantic schemas - for request/response validation
#
# BlogCreate schema - When someone writes a new blog:
# Fields: title, content, category_id (optional)
# Used when creating a new blog post
# author_id will come from authenticated user, not from request
# Example:
# {
#     "title": "My First Blog Post",
#     "content": "This is my amazing blog...",
#     "category_id": 1
# }
#
# BlogUpdate schema - When they want to edit their blog:
# Fields: title (optional), content (optional), category_id (optional), is_published (optional)
# Used when updating an existing blog post
# Example:
# {
#     "title": "My Updated Title",
#     "content": "Updated content...",
#     "category_id": 2,
#     "is_published": true
# }
#
# BlogResponse schema - Full blog details:
# Fields: id, title, content, author_id, category_id, created_at, updated_at, is_published
# Can include nested author info (username, email)
# Used when returning blog data to client
# Example:
# {
#     "id": 1,
#     "title": "My First Blog Post",
#     "content": "This is my amazing blog...",
#     "author_id": 5,
#     "author_username": "john_doe",
#     "category_id": 1,
#     "category_name": "Technology",
#     "is_published": true,
#     "created_at": "2025-01-15T10:30:00",
#     "updated_at": "2025-01-15T14:20:00",
#     "likes_count": 42,
#     "comments_count": 7
# }
#
# BlogListResponse schema - Simpler version for listing many blogs:
# Fields: id, title, author_id, category_id, created_at, is_published
# Example:
# {
#     "id": 1,
#     "title": "My First Blog Post",
#     "author_username": "john_doe",
#     "category_name": "Technology",
#     "created_at": "2025-01-15T10:30:00",
#     "likes_count": 42,
#     "is_published": true
# }
#
# Validation rules:
# - title: 5-200 characters, required
# - content: minimum 10 characters, required