import re
from app.utils.shell import run_command_safe

def sanitize_url(target: str) -> str:
    return target.strip().split()[0] if target.startswith("http") else "http://" + target.strip().split()[0]

def run_nuclei_scan(target: str) -> str:
    sanitized = sanitize_url(target)
    cmd = ["nuclei", "-u", sanitized, "-t", "cves/", "-severity", "critical,high", "-timeout", "60"]
    return run_command_safe(cmd, timeout=300)
