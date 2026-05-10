# microservicio
Este repositorio contiene el código del microservicio,  las pruebas, los workflows de GitHub Actions y los despliegues a PRE y PRO

# EcoAnalyzer – Microservicio PowerShell + Pode

Microservicio que analiza texto y estima una huella de carbono simulada basada en su longitud.

## Endpoints

### GET /analyze?text=hola
Devuelve:
- texto analizado
- entorno (PRE/PRO)
- huella de carbono estimada
- estado

### GET /health
Devuelve:
- estado del servicio
- versión

## Tecnologías
- PowerShell 7
- Pode Framework
- GitHub Actions
- Azure App Service
