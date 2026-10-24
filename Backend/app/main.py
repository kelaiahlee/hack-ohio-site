from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.init_db import init_db
from app.routers import jobs

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()  # creates data/app.db and the three tables if missing
    yield

app = FastAPI(title="Image to Sound", lifespan=lifespan)
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])

@app.get("/health")
def health():
    return {"status": "ok"}