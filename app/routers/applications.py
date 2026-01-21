from fastapi import APIRouter

router = APIRouter()

@router.post("/applications")
def create_application(application: dict):
    return {
        "status": "PENDING",
        "data": application
    }
