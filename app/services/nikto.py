import re
from app.utils.shell import run_command_safe

def sanitize_target(target: str) -> str:
    cleaned = re.sub(r'^(https?://)?(www\.)?', '', target.strip(), flags=re.IGNORECASE)
    host = cleaned.split('/')[0]
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host format.")
    return host

def run_nikto_scan(target: str) -> str:
    try:
        sanitized = sanitize_target(target)
        cmd = ["perl", "/opt/nikto/nikto.pl", "-host", sanitized, "-Tuning", "x", "-ask", "no"]
        return run_command_safe(cmd, timeout=300)
    except Exception as e:
        return f"Error ejecutando Nikto: {str(e)}"
