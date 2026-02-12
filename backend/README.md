# Backend — Lateralus API

FastAPI + LangGraph backend powering the AI agents and CRM logic.

## Prerequisites

| Tool | Version | Purpose |
|------|---------|---------|
| [Docker](https://docs.docker.com/get-docker/) | 20+ | Run PostgreSQL |
| [Node.js](https://nodejs.org/) | 18+ | Run Prisma CLI |
| [Python](https://www.python.org/) | 3.11+ | FastAPI server |

## Quick Start

### 1. Environment variables

```bash
cp .env.example .env
# Then edit .env with your own secrets if needed
```

### 2. Start the database

From the **project root** (where `docker-compose.yml` lives):

```bash
docker compose up -d
```

> This spins up a PostgreSQL 15 instance on `localhost:5432`.  
> Data is persisted in the `postgres_data` Docker volume.

### 3. Run Prisma migrations

```bash
# From the backend/ directory
npx prisma migrate dev --name init
```

This will:
- Create the database tables defined in `prisma/schema.prisma`.
- Generate the Prisma Client for type-safe database access.

### 4. Create a Python virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 5. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the server

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at **http://localhost:8000**.  
Interactive docs at **http://localhost:8000/docs**.

## Database Management

| Command | Description |
|---------|-------------|
| `npx prisma migrate dev` | Apply pending migrations |
| `npx prisma studio` | Open the visual database browser |
| `npx prisma generate` | Re-generate the Prisma Client |
| `npx prisma db push` | Push schema without a migration file |
| `docker compose down` | Stop the database |
| `docker compose down -v` | Stop + wipe all data |

## Folder Structure

```
backend/
├── app/
│   ├── agents/         # LangGraph AI agents & workflows
│   ├── core/           # Config, DB, shared utilities
│   ├── __init__.py
│   └── main.py         # FastAPI entry point
├── prisma/
│   └── schema.prisma   # Database schema (source of truth)
├── requirements.txt
├── .env.example
└── README.md           # ← You are here
```
