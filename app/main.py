from fastapi import FastAPI
from app.config import settings
from app.db.session import engine
from app.db.base import Base
# Import models (VERY IMPORTANT)
from app.models import business, faq

# Import routers (we will create these next)
from app.api import webhook

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

# Include routers
app.include_router(webhook.router, prefix="/webhook", tags=["Webhook"])


# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "app": settings.APP_NAME
    }