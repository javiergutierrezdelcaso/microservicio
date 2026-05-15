# ecoanalyzer

Microservicio **FastAPI** para análisis ecológico, preparado para despliegue profesional y CI/CD.

## Características

- API basada en **FastAPI**
- Endpoint de salud: `/health`
- Endpoint de análisis: `/analysis`
- Tests automatizados con **pytest**
- Integración continua con **GitHub Actions**

## Estructura del proyecto

- `app/`
  - `main.py`: punto de entrada de la aplicación FastAPI
  - `routers/health.py`: endpoint de salud
  - `routers/analysis.py`: endpoint de análisis ecológico
- `tests/`: tests automatizados
- `.github/workflows/microservice-ci.yml`: pipeline de CI
- `requirements.txt`: dependencias de Python

## Desarrollo local

Instalar dependencias:

```bash
pip install -r requirements.txt
