from fastapi import APIRouter

router = APIRouter(
    prefix="/analysis",
    tags=["analysis"]
)


@router.get("")
def analyze():
    # Aquí luego puedes meter lógica real de análisis ecológico
    return {"result": "eco-analysis-ok"}
