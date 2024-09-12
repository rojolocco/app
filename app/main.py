from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

# Verifica si la aplicación está en producción
is_production = os.getenv("ENV") == "production"

# Configura la aplicación FastAPI
app = FastAPI(
    docs_url=None if is_production else "/docs",
    redoc_url=None if is_production else "/redoc",
    openapi_url=None if is_production else "/openapi.json"
)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <h1>Hello, Christian</h1>
        </body>
    </html>
    """

@app.get("/about")
def about():
    return {"About": "Christian"}