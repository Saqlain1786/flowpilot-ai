from app.storage import save_note

def create_note(user_id: str, message: str):
    note_data = {
        "note_id": "note_001",
        "title": "Meeting Note",
        "content": "Auto-saved note from user request",
        "created_for_user": user_id
    }

    save_note(note_data)

    return {
        "agent": "notes_agent",
        "action": "create_note",
        "status": "success",
        "note": note_data,
        "source_message": message
    }