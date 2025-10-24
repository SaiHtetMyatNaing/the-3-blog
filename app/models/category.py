# Category model - represents blog categories in the database
# Fields to include:
# - id: primary key
# - name: category name (unique)
# - description: category description (optional)
# - created_at: timestamp when category was created
# Relationships:
# - blogs: one category can have many blogs

# Example data structure:
# {
#     "id": 1,
#     "name": "Technology",
#     "description": "All about tech stuff",
#     "created_at": "2025-01-15T10:30:00"
# }