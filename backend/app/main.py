"""
Lateralus — FastAPI Backend
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import prisma
from app.routers.job_router import router as job_router
from app.routers.user_router import router as user_router


# ---------------------------------------------------------------------------
# Lifespan — Prisma connect / disconnect
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage the Prisma client connection across the app lifecycle."""
    await prisma.connect()
    yield
    await prisma.disconnect()


# ---------------------------------------------------------------------------
# Application factory
# ---------------------------------------------------------------------------
app = FastAPI(
    title="Lateralus API",
    description="AI-powered CRM backend for intelligent job hunting",
    version="0.1.0",
    lifespan=lifespan,
)

# ---------------------------------------------------------------------------
# CORS — allow the Next.js frontend & Chrome extension to reach us
# ---------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Register routers
# ---------------------------------------------------------------------------
app.include_router(user_router, prefix="/api/v1")
app.include_router(job_router, prefix="/api/v1")


# ---------------------------------------------------------------------------
# Health / Root
# ---------------------------------------------------------------------------
@app.get("/")
async def root():
    return {"message": "🚀 Lateralus API is running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}
