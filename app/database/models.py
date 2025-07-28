# app/database/models.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ScanResult(Base):
    __tablename__ = "scan_results"

    id = Column(Integer, primary_key=True, index=True)
    target = Column(String, index=True)
    nmap = Column(Text)
    whatweb = Column(Text)
    nikto = Column(Text)
    nuclei = Column(Text)
    headers = Column(Text)
    waf = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
