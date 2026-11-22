from fastapi import FastAPI

app = FastAPI(
    title="Inventory Management API",
    description="Backend API for our Inventory Management System",
    version="1.0.0",
)

@app.get("/")
def root():
    return {"message": "Everything works well"}

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }