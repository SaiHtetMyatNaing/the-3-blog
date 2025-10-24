# Category Pydantic schemas - for request/response validation
#
# CategoryCreate schema:
# - Fields: name, description (optional)
# - Used when creating a new category
#
# CategoryUpdate schema:
# - Fields: name (optional), description (optional)
# - Used when updating a category
#
# CategoryResponse schema:
# - Fields: id, name, description, created_at
# - Used when returning category data to client