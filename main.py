from fastapi import FastAPI
from pydantic import BaseModel
from app.orchestrator import handle_request
from app.storage import get_workflows, get_events, get_tasks, get_notes

app = FastAPI()


# Request model
class ChatRequest(BaseModel):
    user_id: str
    message: str


# Root endpoint (VERY important for Cloud Run)
@app.get("/")
def home():
    return {
        "app": "FlowPilot AI",
        "status": "running",
        "message": "Multi-Agent Productivity Assistant is live"
    }


# Main chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    result = handle_request(request.user_id, request.message)
    return result


# (Optional but already supported in your backend)
@app.get("/workflows")
def fetch_workflows():
    return get_workflows()


@app.get("/events")
def fetch_events():
    return get_events()


@app.get("/tasks")
def fetch_tasks():
    return get_tasks()


@app.get("/notes")
def fetch_notes():
    return get_notes()
