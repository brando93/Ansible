from fastapi import FastAPI, HTTPException
from app.schemas import PredictRequest, PredictResponse
from app.model import model
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ENV = os.getenv("ENV", "unknown")

app = FastAPI(
    title="AI API",
    description=f"Environment: {ENV}"
)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "environment": ENV
    }

@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    try:
        result = model.predict(payload.text)
        logger.info("Prediction executed")
        return PredictResponse(result=result)
    except Exception:
        logger.exception("Prediction failed")
        raise HTTPException(status_code=500, detail="Internal error")