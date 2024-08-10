import uvicorn
from fastapi import FastAPI
from .routers import items, task, info

app = FastAPI()

app.include_router(items.router)
app.include_router(task.router)
app.include_router(info.router)


def dev():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
