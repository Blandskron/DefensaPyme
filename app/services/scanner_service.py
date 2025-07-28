import shutil
from typing import Dict

from app.services.nmap import run_nmap_scan
from app.services.whatweb import run_whatweb_scan
from app.services.nikto import run_nikto_scan
from app.services.nuclei import run_nuclei_scan
from app.services.headers import analyze_security_headers
from app.services.waf import detect_waf


def is_tool_installed(tool_name: str) -> bool:
    return shutil.which(tool_name) is not None


def run_scans(target: str) -> Dict[str, str | dict]:
    results = {}

    try:
        results["nmap"] = run_nmap_scan(target) if is_tool_installed("nmap") else "Error: Nmap no está instalado."
    except Exception as e:
        results["nmap"] = f"Error: {str(e)}"

    try:
        results["whatweb"] = run_whatweb_scan(target) if is_tool_installed("whatweb") else "Error: WhatWeb no está instalado."
    except Exception as e:
        results["whatweb"] = f"Error: {str(e)}"

    try:
        results["nikto"] = run_nikto_scan(target) if is_tool_installed("perl") else "Error: Perl o Nikto no están instalados."
    except Exception as e:
        results["nikto"] = f"Error: {str(e)}"

    try:
        results["nuclei"] = run_nuclei_scan(target) if is_tool_installed("nuclei") else "Error: Nuclei no está instalado."
    except Exception as e:
        results["nuclei"] = f"Error: {str(e)}"

    try:
        results["headers"] = analyze_security_headers(target)
    except Exception as e:
        results["headers"] = {"error": str(e)}

    try:
        results["waf"] = detect_waf(target) if is_tool_installed("wafw00f") else "Error: wafw00f no está instalado."
    except Exception as e:
        results["waf"] = f"Error: {str(e)}"

    return results
