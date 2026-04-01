# FlowPilot AI 🚀

Multi-Agent Productivity Assistant powered by FastAPI and deployed on Google Cloud Run.

---

## 🧠 Problem
Users rely on multiple tools (calendar, tasks, notes) but lack a unified system to execute multi-step workflows from a single request.

---

## 💡 Solution
FlowPilot AI acts as an orchestrator that:
- Interprets user intent
- Breaks it into actions
- Delegates to specialized agents
- Executes workflows
- Stores structured results

---

## ⚙️ Architecture

- FastAPI (API layer)
- Orchestrator Engine
- Modular Agents:
  - Calendar Agent
  - Task Agent
  - Notes Agent
- JSON-based persistence
- Dockerized deployment
- Google Cloud Run hosting

---

## 🔥 Demo Use Case

### Input:
```json
{
  "user_id": "user_001",
  "message": "Schedule a meeting and create a task and save a note"
}
