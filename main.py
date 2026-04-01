from app.storage import save_event

def create_event(user_id: str, message: str):
    event_data = {
        "event_id": "evt_001",
        "title": "Scheduled Meeting",
        "scheduled_for": "tomorrow at 3 PM",
        "created_for_user": user_id
    }

    save_event(event_data)

    return {
        "agent": "calendar_agent",
        "action": "create_event",
        "status": "success",
        "event": event_data,
        "source_message": message
    }