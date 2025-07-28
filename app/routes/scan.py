from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.nmap import run_nmap_scan
from app.services.whatweb import run_whatweb_scan
from app.services.nikto import run_nikto_scan
from app.services.nuclei import run_nuclei_scan
from app.services.headers import analyze_security_headers
from app.services.waf import detect_waf


router = APIRouter()

class ScanRequest(BaseModel):
    target: str  # Permitir dominio, IP o URL

@router.post("/scan")
async def scan_target(request: ScanRequest):
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
        return {"success": True, "data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

