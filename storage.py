from app.calendar_agent import create_event
from app.task_agent import create_task
from app.notes_agent import create_note
from app.storage import save_workflow
import uuid
from datetime import datetime


def handle_request(user_id: str, message: str):
    actions = []
    results = []

    workflow_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    if "meeting" in message.lower():
        actions.append("calendar_agent:create_event")
        results.append(create_event(user_id, message))

    if "task" in message.lower():
        actions.append("task_agent:create_task")
        results.append(create_task(user_id, message))

    if "note" in message.lower():
        actions.append("notes_agent:create_note")
        results.append(create_note(user_id, message))

    summary_parts = []

    if any(r.get("agent") == "calendar_agent" for r in results):
        summary_parts.append("meeting scheduled")

    if any(r.get("agent") == "task_agent" for r in results):
        summary_parts.append("task created")

    if any(r.get("agent") == "notes_agent" for r in results):
        summary_parts.append("note saved")

    summary = "Workflow completed: " + ", ".join(summary_parts) + "."

    workflow_data = {
        "workflow_id": workflow_id,
        "timestamp": timestamp,
        "user_id": user_id,
        "original_message": message,
        "summary": summary,
        "actions_planned": actions,
        "agent_results": results,
        "status": "orchestrated"
    }

    save_workflow(workflow_data)

    return workflow_data