"""API routes for the JobProcess domain."""

from fastapi import APIRouter, HTTPException, Query

from app.schemas.job import JobProcessCreate, JobProcessResponse
from app.services import job_service, user_service

router = APIRouter(prefix="/jobs", tags=["Job Processes"])


# ---------------------------------------------------------------------------
# POST /jobs — create a new job process
# ---------------------------------------------------------------------------
@router.post("/", response_model=JobProcessResponse, status_code=201)
async def create_job(payload: JobProcessCreate):
    """Create a new job process. Validates that the referenced user exists."""
    user = await user_service.get_user_by_id(payload.userId)
    if not user:
        raise HTTPException(status_code=404, detail="Referenced user not found")

    job = await job_service.create_job_process(payload)
    return job


# ---------------------------------------------------------------------------
# GET /jobs/{job_id} — retrieve a single job process
# ---------------------------------------------------------------------------
@router.get("/{job_id}", response_model=JobProcessResponse)
async def get_job(job_id: str):
    """Fetch a single job process by its ID. Returns 404 if not found."""
    job = await job_service.get_job_process_by_id(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job process not found")
    return job


# ---------------------------------------------------------------------------
# GET /jobs/user/{user_id} — list all job processes for a user
# ---------------------------------------------------------------------------
@router.get("/user/{user_id}", response_model=list[JobProcessResponse])
async def list_jobs_for_user(
    user_id: str,
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    take: int = Query(50, ge=1, le=100, description="Number of records to return"),
):
    """Return all job processes belonging to a specific user (paginated)."""
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return await job_service.list_jobs_by_user(user_id, skip=skip, take=take)
