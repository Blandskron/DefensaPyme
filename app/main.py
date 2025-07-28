from fastapi import FastAPI
from app.routes.scan import router as scan_router

app = FastAPI(
    title="DefensaPyme - API de Escaneo de Seguridad",
    version="0.1.0"
)

app.include_router(scan_router, prefix="/api")
