from fastapi import FastAPI

app = FastAPI(title="Credit Approval API")

@app.get("/")
def root():
    return {"message": "API running"}
