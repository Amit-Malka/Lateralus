"""
Job-Hunter-AI-CRM — FastAPI Backend
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Job-Hunter-AI-CRM API",
    description="AI-powered CRM backend for intelligent job hunting",
    version="0.1.0",
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
# Health / Hello World
# ---------------------------------------------------------------------------
@app.get("/")
async def root():
    return {"message": "🚀 Job-Hunter-AI-CRM API is running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}
