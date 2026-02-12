"""CRUD service layer for the User domain."""

from prisma.models import User

from app.core.database import prisma
from app.schemas.user import UserCreate


async def create_user(data: UserCreate) -> User:
    """Create a new user in the database."""
    return await prisma.user.create(
        data={
            "email": data.email,
            "name": data.name,
        }
    )


async def get_user_by_id(user_id: str) -> User | None:
    """Return a user by primary key, or ``None`` if not found."""
    return await prisma.user.find_unique(where={"id": user_id})


async def get_user_by_email(email: str) -> User | None:
    """Return a user by email address, or ``None`` if not found."""
    return await prisma.user.find_unique(where={"email": email})


async def list_users(skip: int = 0, take: int = 50) -> list[User]:
    """Return a paginated list of users."""
    return await prisma.user.find_many(skip=skip, take=take, order={"createdAt": "desc"})
