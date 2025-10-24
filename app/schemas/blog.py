# Blog Pydantic schemas - for request/response validation
#
# BlogCreate schema:
# - Fields: title, content, category_id (optional)
# - Used when creating a new blog post
# - author_id will come from authenticated user, not from request
#
# BlogUpdate schema:
# - Fields: title (optional), content (optional), category_id (optional), is_published (optional)
# - Used when updating an existing blog post
#
# BlogResponse schema:
# - Fields: id, title, content, author_id, category_id, created_at, updated_at, is_published
# - Can include nested author info (username, email)
# - Used when returning blog data to client
#
# BlogListResponse schema:
# - Simpler version with fewer fields for listing many blogs
# - Fields: id, title, author_id, category_id, created_at, is_published