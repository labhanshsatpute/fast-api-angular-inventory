from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title="Inventory Management API",
    description="Backend API for our Inventory Management System",
    version="1.0.0",
    debug=settings.DEBUG
)

@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} is running",
        "enviorment": settings.APP_ENV,
        "status": "success"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }