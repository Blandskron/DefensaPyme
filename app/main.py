from fastapi import FastAPI
from app.routes.scan import router as scan_router
from app.database.database import engine
from app.database.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DefensaPyme - API de Escaneo de Seguridad",
    version="0.1.0"
)

app.include_router(scan_router, prefix="/api")
