from fastapi import FastAPI
from .routers import items, task, info

app = FastAPI()

app.include_router(items.router)
app.include_router(task.router)
app.include_router(info.router)
