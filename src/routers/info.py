from fastapi import APIRouter

router = APIRouter(
    prefix="/info",
)


@router.get("/")
def info():
    return {"status": "running"}
