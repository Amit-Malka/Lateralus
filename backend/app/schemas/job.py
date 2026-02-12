"""Pydantic schemas for the JobProcess domain."""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


# ---------------------------------------------------------------------------
# Mirror the Prisma ProcessStatus enum
# ---------------------------------------------------------------------------
class ProcessStatus(str, Enum):
    IDENTIFIED = "IDENTIFIED"
    APPLIED = "APPLIED"
    INTERVIEW = "INTERVIEW"
    OFFER = "OFFER"
    REJECTED = "REJECTED"


# ---------------------------------------------------------------------------
# Request schemas
# ---------------------------------------------------------------------------
class JobProcessCreate(BaseModel):
    """Payload accepted when creating a new job process."""

    userId: str
    companyName: str
    role: str
    status: ProcessStatus = ProcessStatus.IDENTIFIED
    jobDescription: Optional[str] = None
    link: Optional[str] = None


# ---------------------------------------------------------------------------
# Response schemas
# ---------------------------------------------------------------------------
class JobProcessResponse(BaseModel):
    """Public representation of a JobProcess returned by the API."""

    id: str
    userId: str
    companyName: str
    role: str
    status: ProcessStatus
    jobDescription: Optional[str] = None
    link: Optional[str] = None
    createdAt: datetime

    model_config = {"from_attributes": True}
