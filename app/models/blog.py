# Blog model - represents blog posts in the database
# Fields to include:
# - id: primary key
# - title: blog post title
# - content: blog post content/body
# - author_id: foreign key to User (who wrote this blog)
# - category_id: foreign key to Category (optional)
# - created_at: timestamp when blog was created
# - updated_at: timestamp of last update
# - is_published: boolean to track if blog is published
# Relationships:
# - author: many blogs belong to one user
# - category: many blogs can belong to one category
# - comments: one blog can have many comments
# - likes: one blog can have many likes

# Example data structure:
# {
#     "id": 1,
#     "title": "My First Blog Post",
#     "content": "This is my amazing blog content...",
#     "author_id": 5,
#     "category_id": 1,
#     "is_published": true,
#     "created_at": "2025-01-15T10:30:00",
#     "updated_at": "2025-01-15T14:20:00"
# }