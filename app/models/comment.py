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