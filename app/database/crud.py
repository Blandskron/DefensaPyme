from sqlalchemy.orm import Session
from app.database.models import ScanResult

def save_scan_result(db: Session, target: str, data: dict):
    scan = ScanResult(
        target=target,
        nmap=data.get("nmap"),
        whatweb=data.get("whatweb"),
        nikto=data.get("nikto"),
        nuclei=data.get("nuclei"),
        headers=str(data.get("headers")),  # serializamos dict
        waf=data.get("waf")
    )
    db.add(scan)
    db.commit()
    db.refresh(scan)
    return scan
