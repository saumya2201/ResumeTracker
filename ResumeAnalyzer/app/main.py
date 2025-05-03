from fastapi import FastAPI
from app.api import resume_routes

app = FastAPI(title="Resume Analyzer API")

# Include router
app.include_router(resume_routes.router, prefix="/api")

@app.get("/ping")
def ping():
    return {"message": "pong"}
