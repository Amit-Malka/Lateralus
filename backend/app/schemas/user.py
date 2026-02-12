"""Pydantic schemas for the User domain."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


# ---------------------------------------------------------------------------
# Request schemas
# ---------------------------------------------------------------------------
class UserCreate(BaseModel):
    """Payload accepted when creating a new user."""

    email: EmailStr
    name: Optional[str] = None


# ---------------------------------------------------------------------------
# Response schemas
# ---------------------------------------------------------------------------
class UserResponse(BaseModel):
    """Public representation of a User returned by the API."""

    id: str
    email: str
    name: Optional[str] = None
    createdAt: datetime

    model_config = {"from_attributes": True}
