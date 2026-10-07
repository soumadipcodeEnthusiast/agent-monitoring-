from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class AgentRunResult(BaseModel):
    success: bool
    final_answer: Optional[str]
    trace_id: str
    
class TraceStep(BaseModel):
    step_id: str
    type: str
    timestamp: datetime
    input: Optional[str] = None
    output: Optional[str] = None
    tool: Optional[str] = None
    arguments: Optional[Dict[str, Any]] = None
    result: Optional[Dict[str, Any]] = None
    latency_ms: Optional[int] = None

class Trace(BaseModel):
    run_id: str
    task: str
    started_at: datetime
    completed_at: datetime
    steps: List[TraceStep]
    final_answer: Optional[str] = None
    success: bool

class ExperimentCreate(BaseModel):
    agent_id: str
    task: str
    strategy: str

class MetricOverview(BaseModel):
    total_experiments: int
    failures_discovered: int
    unique_failure_patterns: int
    average_failure_boundary: float
    recovery_rate: float
    adaptive_advantage: float
