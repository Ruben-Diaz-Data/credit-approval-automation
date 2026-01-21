from fastapi import APIRouter, UploadFile, File
from app.schemas.application import ApplicationCreate
import uuid
import random

router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)

@router.post("/")
def create_application(application: ApplicationCreate):
    return {
        "application_id": str(uuid.uuid4()),
        "status": "PENDING",
        "applicant": application
    }

@router.post("/{app_id}/documents")
def upload_document(app_id: str, file: UploadFile = File(...)):
    return {
        "application_id": app_id,
        "filename": file.filename,
        "extracted_address": "Calle Falsa 123, CDMX"
    }

@router.get("/scorecredito")
def score_credito():
    return {
        "score": random.randint(300, 900)
    }

@router.post("/{app_id}/evaluate")
def evaluate_application(app_id: str, income: float, score: int):
    decision = "REJECTED"
    reasons = []

    if income > 15000:
        reasons.append("Income above minimum")
    else:
        reasons.append("Income below minimum")

    if score >= 500:
        reasons.append("Score accepted")
    else:
        reasons.append("Score too low")

    if income > 15000 and score >= 500:
        decision = "APPROVED"

    return {
        "application_id": app_id,
        "decision": decision,
        "reasons": reasons
    }
