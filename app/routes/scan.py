from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.services.nmap import run_nmap_scan
from app.services.whatweb import run_whatweb_scan
from app.services.nikto import run_nikto_scan
from app.services.nuclei import run_nuclei_scan
from app.services.headers import analyze_security_headers
from app.services.waf import detect_waf

from app.database.database import SessionLocal
from app.database.crud import save_scan_result

router = APIRouter()

class ScanRequest(BaseModel):
    target: str  # Dominio, IP o URL


# Dependency para la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/scan")
async def scan_target(request: ScanRequest, db: Session = Depends(get_db)):
    try:
        target = request.target
        results = {
            "nmap": run_nmap_scan(target),
            "whatweb": run_whatweb_scan(target),
            "nikto": run_nikto_scan(target),
            "nuclei": run_nuclei_scan(target),
            "headers": analyze_security_headers(target),
            "waf": detect_waf(target),
        }

        # Guardar en base de datos
        save_scan_result(db=db, target=target, data=results)

        return {"success": True, "data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
