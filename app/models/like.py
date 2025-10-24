# Like model - represents likes on blog posts
# Fields to include:
# - id: primary key
# - blog_id: foreign key to Blog (which blog is liked)
# - user_id: foreign key to User (who liked the blog)
# - created_at: timestamp when like was created
# Constraints:
# - Add unique constraint on (blog_id, user_id) so one user can only like a blog once
# Relationships:
# - blog: many likes belong to one blog
# - user: many likes belong to one user