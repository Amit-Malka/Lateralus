# Backend — Job-Hunter-AI-CRM API

FastAPI + LangGraph backend powering the AI agents and CRM logic.

## Quick Start

### 1. Create a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

```bash
cp .env.example .env
# Then edit .env with your API keys (OpenAI, etc.)
```

### 4. Run the server

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at **http://localhost:8000**.  
Interactive docs at **http://localhost:8000/docs**.

## Folder Structure

```
backend/
├── app/
│   ├── agents/       # LangGraph AI agents & workflows
│   ├── core/         # Config, DB, shared utilities
│   ├── __init__.py
│   └── main.py       # FastAPI entry point
├── requirements.txt
├── .env.example
└── README.md         # ← You are here
```
