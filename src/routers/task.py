from fastapi import APIRouter, HTTPException
import httpx
from pydantic import BaseModel


class TaskRequest(BaseModel):
    progressCallbackUrl: str
    completeCallbackUrl: str
    errorCallbackUrl: str


router = APIRouter(
    prefix="/task",
    tags=["task"],
)


# calls back to an endpoint you pass in
@router.post("/{task_id}")
def start_task(task_id: str, body: TaskRequest) -> dict[str, str]:
    response = {"progress": 0, "payload": {"some": "stuff"}}
    try:
        httpx.post(body.progressCallbackUrl, json=response)
        return {"task_id": task_id, "status": "in progress"}
    except httpx.HTTPError as exc:
        print(f"HTTP Exception for {exc.request.url} - {exc}")
        raise HTTPException(status_code=500, detail=str(exc))
