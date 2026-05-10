# Carbon Footprint FastAPI Microservice

Microservicio Python usando FastAPI para estimar la huella de carbono de un texto.

## Uso local

1. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta el servicio:
   ```bash
   uvicorn main:app --reload --port 8080
   ```

## Endpoints

- `/analyze?text=TU_TEXTO` — Devuelve la huella de carbono estimada para el texto.
- `/health` — Health check del microservicio.

## Variables de entorno

- `APP_ENV`: Define el entorno (por defecto: PRE).

## Ejemplo de respuesta

```json
{
  "input": "Hola mundo",
  "environment": "PRE",
  "estimated_carbon_gco2": 0.022,
  "status": "Success"
}
```