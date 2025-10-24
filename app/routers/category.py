from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_categories():
    return {"message": "Category router working"}

# Category router - API endpoints for category operations
#
# Endpoints to implement:
# POST /categories - Create a new category (may require admin rights)
# GET /categories - Get all categories
# GET /categories/{category_id} - Get specific category by ID
# GET /categories/{category_id}/blogs - Get all blogs in a category
# PUT /categories/{category_id} - Update a category (may require admin rights)
# DELETE /categories/{category_id} - Delete a category (may require admin rights)
#
# Remember to:
# - Consider if category operations should be admin-only
# - Return blogs count for each category when listing
# - Handle deletion carefully (what happens to blogs in deleted category?)