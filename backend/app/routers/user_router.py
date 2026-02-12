"""API routes for the User domain."""

from fastapi import APIRouter, HTTPException, Query

from app.schemas.user import UserCreate, UserResponse
from app.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])


# ---------------------------------------------------------------------------
# POST /users — create a new user
# ---------------------------------------------------------------------------
@router.post("/", response_model=UserResponse, status_code=201)
async def create_user(payload: UserCreate):
    """Register a new user. Raises 409 if the email already exists."""
    existing = await user_service.get_user_by_email(payload.email)
    if existing:
        raise HTTPException(status_code=409, detail="A user with this email already exists")

    user = await user_service.create_user(payload)
    return user


# ---------------------------------------------------------------------------
# GET /users/{user_id} — retrieve a user by ID
# ---------------------------------------------------------------------------
@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    """Fetch a single user by their ID. Returns 404 if not found."""
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# ---------------------------------------------------------------------------
# GET /users — list users (paginated)
# ---------------------------------------------------------------------------
@router.get("/", response_model=list[UserResponse])
async def list_users(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    take: int = Query(50, ge=1, le=100, description="Number of records to return"),
):
    """Return a paginated list of users."""
    return await user_service.list_users(skip=skip, take=take)
