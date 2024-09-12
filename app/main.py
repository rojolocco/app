from fastapi import FastAPI
import os

# Verifica si la aplicación está en producción
is_production = os.getenv("ENV") == "production"

# Configura la aplicación FastAPI
app = FastAPI(
    docs_url=None if is_production else "/docs",
    redoc_url=None if is_production else "/redoc",
    openapi_url=None if is_production else "/openapi.json"
)

@app.get("/")
def home():
    return {"Hello": "Christian"}

@app.get("/about")
def about():
    return {"About": "Christian"}