import uvicorn
from fastapi import FastAPI
from .routers import items, task, info

app = FastAPI()

app.include_router(items.router)
app.include_router(task.router)
app.include_router(info.router)


# Run in dev mode with reloading available
def dev():
    """Launched with `pdm run dev` at root level"""
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)


# If we run this file directly, it will start the server
if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000)
