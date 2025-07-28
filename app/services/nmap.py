import re
from app.utils.shell import run_command_safe

def sanitize_target(target: str) -> str:
    cleaned = re.sub(r'^(https?://)?(www\.)?', '', target.strip(), flags=re.IGNORECASE)
    host = cleaned.split('/')[0]
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host format.")
    return host

def run_nmap_scan(target: str) -> str:
    try:
        sanitized = sanitize_target(target)
        cmd = ["nmap", "-sV", "-O", "-Pn", "--script", "vuln", sanitized]
        return run_command_safe(cmd, timeout=180)
    except Exception as e:
        return f"Error ejecutando Nmap: {str(e)}"
