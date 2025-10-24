# Category Pydantic schemas - for request/response validation
#
# CategoryCreate schema - When creating a new category:
# Fields: name, description (optional)
# Used when creating a new category
# Example:
# {
#     "name": "Technology",
#     "description": "All about tech stuff"
# }
#
# CategoryUpdate schema - When updating a category:
# Fields: name (optional), description (optional)
# Used when updating a category
# Example:
# {
#     "name": "Tech & Gadgets",
#     "description": "Updated description"
# }
#
# CategoryResponse schema - Category details:
# Fields: id, name, description, created_at
# Used when returning category data to client
# Example:
# {
#     "id": 1,
#     "name": "Technology",
#     "description": "All about tech stuff",
#     "created_at": "2025-01-15T10:30:00",
#     "blogs_count": 15
# }
#
# Validation rules:
# - name: 2-50 characters, required, unique
# - description: optional