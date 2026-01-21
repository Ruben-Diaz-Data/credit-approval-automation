from fastapi import FastAPI
from app.routers import applications

app = FastAPI(title="Credit Approval API")

app.include_router(applications.router)

@app.get("/")
def root():
    return {"message": "API running"}
