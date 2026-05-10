from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import os

app = FastAPI(title="Carbon Footprint Microservice", version="1.1.0")

@app.get("/analyze")
def analyze(text: str = Query(..., description="Texto a analizar")):
    env = os.getenv("APP_ENV", "PRE")
    carbon_footprint = len(text) * 0.002
    return JSONResponse({
        "input": text,
        "environment": env,
        "estimated_carbon_gco2": carbon_footprint,
        "status": "Success"
    })

@app.get("/health")
def health():
    return JSONResponse({
        "status": "Healthy",
        "version": "1.1.0"
    })