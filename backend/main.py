from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import EventRequest, NudgeResponse, ApprovalRequest, HealthScoreResponse, AuditLogEntry
from database import init_db, get_user_memory, log_event, get_db
from agent_orchestrator import process_event_with_agents
import uvicorn

app = FastAPI(title="SBI Smart Financial Coach API")

# Setup CORS for Vite frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    init_db()
    log_event("SYSTEM_START", "Initialized SBI Smart Coach MVP")

@app.post("/trigger_event", response_model=NudgeResponse)
def trigger_event(request: EventRequest):
    user_memory = get_user_memory()
    
    # Update balance based on event
    if request.event_type == "Salary Credited":
        new_balance = user_memory["balance"] + request.amount
        with get_db() as conn:
            conn.execute("UPDATE user_memory SET balance = ? WHERE id = 1", (new_balance,))
            conn.commit()
        
    log_event("EVENT_DETECTED", f"Detected {request.event_type} of ₹{request.amount:,.2f}")
    
    # Orchestrate Agents
    recommendations = process_event_with_agents(request.event_type, request.amount, user_memory)
    
    log_event("NUDGES_GENERATED", f"Generated {len(recommendations)} recommendations")
    return NudgeResponse(recommendations=recommendations)

@app.post("/respond_to_nudge")
def respond_to_nudge(request: ApprovalRequest):
    status = request.action
    log_event("USER_RESPONSE", f"User {status} recommendation {request.recommendation_id}")
    
    if status == "APPROVE":
        # In a real app, this would execute the transaction
        pass
    
    return {"status": "success", "message": f"Action {status} recorded"}

@app.get("/health_score", response_model=HealthScoreResponse)
def get_health_score():
    # Mock health score calculation based on user memory
    user_memory = get_user_memory()
    
    return HealthScoreResponse(
        score=82,
        income_stability=True,
        savings=True,
        emergency_fund=True,
        investments=False,
        insurance=False,
        credit_utilization=False
    )

@app.get("/audit_logs", response_model=list[AuditLogEntry])
def get_audit_logs():
    with get_db() as conn:
        cursor = conn.execute("SELECT * FROM audit_log ORDER BY timestamp DESC LIMIT 20")
        rows = cursor.fetchall()
        
    return [
        AuditLogEntry(
            id=row["id"],
            timestamp=row["timestamp"],
            event_type=row["event_type"],
            details=row["details"],
            status=row["status"]
        ) for row in rows
    ]

@app.get("/memory")
def get_memory():
    return get_user_memory()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
