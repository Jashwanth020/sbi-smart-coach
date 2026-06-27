from pydantic import BaseModel
from typing import List, Optional

class EventRequest(BaseModel):
    event_type: str
    amount: float
    description: str

class Recommendation(BaseModel):
    id: str
    title: str
    description: str
    action_text: str
    amount: Optional[float] = None
    category: str

class NudgeResponse(BaseModel):
    recommendations: List[Recommendation]

class ApprovalRequest(BaseModel):
    recommendation_id: str
    action: str # "APPROVE" or "REJECT"

class AuditLogEntry(BaseModel):
    id: int
    timestamp: str
    event_type: str
    details: str
    status: str

class HealthScoreResponse(BaseModel):
    score: int
    income_stability: bool
    savings: bool
    emergency_fund: bool
    investments: bool
    insurance: bool
    credit_utilization: bool
