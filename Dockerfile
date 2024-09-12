# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . .

# Instala Poetry
RUN pip install poetry

# Instala las dependencias del proyecto
RUN poetry install --no-root

# Expone el puerto en el que correrá la aplicación
EXPOSE 8000

# Define el comando para iniciar el servidor de FastAPI con uvicorn
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]