# Comment model - represents comments on blog posts
# Fields to include:
# - id: primary key
# - content: comment text
# - blog_id: foreign key to Blog (which blog this comment is on)
# - user_id: foreign key to User (who wrote this comment)
# - created_at: timestamp when comment was created
# - updated_at: timestamp of last update
# Relationships:
# - blog: many comments belong to one blog
# - user: many comments belong to one user

# Example data structure:
# {
#     "id": 1,
#     "content": "Great blog post!",
#     "blog_id": 1,
#     "user_id": 5,
#     "created_at": "2025-01-15T10:30:00",
#     "updated_at": "2025-01-15T10:30:00"
# }