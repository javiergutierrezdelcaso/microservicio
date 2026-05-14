from fastapi import FastAPI

from .routers import analysis, health

app = FastAPI(
    title="ecoanalyzer",
    version="1.0.0",
    description="Microservicio FastAPI para análisis ecológico.",
)

app.include_router(health.router)
app.include_router(analysis.router)


@app.get("/")
def root():
    return {"service": "ecoanalyzer", "status": "running"}
