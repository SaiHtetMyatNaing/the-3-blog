from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_categories():
    return {"message": "Category router working"}

# Category router - API endpoints for category operations
#
# Endpoints to implement:
# 
# POST /categories - Create a new category (may require admin rights)
# Request body example:
# {
#     "name": "Technology",
#     "description": "All about tech stuff"
# }
# Response example:
# {
#     "id": 1,
#     "name": "Technology",
#     "description": "All about tech stuff",
#     "created_at": "2025-01-15T10:30:00"
# }
#
# GET /categories - Get all categories
# Response example:
# [
#     {
#         "id": 1,
#         "name": "Technology",
#         "description": "All about tech stuff",
#         "blogs_count": 15
#     },
#     {
#         "id": 2,
#         "name": "Travel",
#         "description": "Travel experiences",
#         "blogs_count": 8
#     }
# ]
#
# GET /categories/{category_id} - Get specific category by ID
# Response example: single category with blogs count
#
# GET /categories/{category_id}/blogs - Get all blogs in a category
# Response example: list of blogs in that category
#
# PUT /categories/{category_id} - Update a category (may require admin rights)
# Request body example:
# {
#     "name": "Tech & Gadgets",
#     "description": "Updated description"
# }
#
# DELETE /categories/{category_id} - Delete a category (may require admin rights)
#
# Remember to:
# - Consider if category operations should be admin-only
# - Return blogs count for each category when listing
# - Handle deletion carefully (what happens to blogs in deleted category?)