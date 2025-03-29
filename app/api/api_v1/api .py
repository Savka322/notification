from fastapi import APIRouter

router = APIRouter()

# Define your endpoints here
# For example:
@router.get("/example")
async def example_endpoint():
    return {"message": "This is an example"}