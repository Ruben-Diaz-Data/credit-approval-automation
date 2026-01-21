from pydantic import BaseModel

class ApplicationCreate(BaseModel):
    name: str
    rfc: str
    curp: str
    age: int
    monthly_income: float
