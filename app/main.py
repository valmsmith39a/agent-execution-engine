from fastapi import FastAPI

from app.core.config import settings
from app.routes.health import router as health_router
from app.routes.jobs import router as jobs_router

app = FastAPI(title=settings.app_name)
app.include_router(health_router)
app.include_router(jobs_router)
