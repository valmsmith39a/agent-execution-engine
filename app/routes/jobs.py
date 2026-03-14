from typing import Any, Dict

from fastapi import APIRouter, status
from pydantic import BaseModel

from app.queue import enqueue

router = APIRouter()


class CreateJobRequest(BaseModel):
    task_type: str
    payload: Dict[str, Any]


class CreateJobResponse(BaseModel):
    job_id: str
    status: str


@router.post("/jobs", status_code=status.HTTP_201_CREATED, response_model=CreateJobResponse)
def create_job(job: CreateJobRequest) -> CreateJobResponse:
    _ = job
    job_id = "stub-job-1"
    enqueue(job_id)
    return CreateJobResponse(job_id=job_id, status="queued")
