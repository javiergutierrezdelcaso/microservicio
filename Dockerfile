FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar requirements desde la carpeta ecoanalyzer
COPY ecoanalyzer/requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código del microservicio
COPY ecoanalyzer/ .

# Exponer el puerto donde correrá FastAPI
EXPOSE 8000

# Comando de arranque del microservicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
