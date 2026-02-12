"""CRUD service layer for the JobProcess domain."""

from prisma.models import JobProcess

from app.core.database import prisma
from app.schemas.job import JobProcessCreate


async def create_job_process(data: JobProcessCreate) -> JobProcess:
    """Create a new job process linked to an existing user."""
    return await prisma.jobprocess.create(
        data={
            "userId": data.userId,
            "companyName": data.companyName,
            "role": data.role,
            "status": data.status.value,
            "jobDescription": data.jobDescription,
            "link": data.link,
        }
    )


async def get_job_process_by_id(job_id: str) -> JobProcess | None:
    """Return a single job process by primary key."""
    return await prisma.jobprocess.find_unique(where={"id": job_id})


async def list_jobs_by_user(user_id: str, skip: int = 0, take: int = 50) -> list[JobProcess]:
    """Return all job processes belonging to a specific user (paginated)."""
    return await prisma.jobprocess.find_many(
        where={"userId": user_id},
        skip=skip,
        take=take,
        order={"createdAt": "desc"},
    )
