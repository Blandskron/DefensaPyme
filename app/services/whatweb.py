import re
from app.utils.shell import run_command_safe

def sanitize_url(target: str) -> str:
    return target.strip().split()[0] if target.startswith("http") else "http://" + target.strip().split()[0]

def run_whatweb_scan(target: str) -> str:
    cmd = ["whatweb", "--no-errors", "--color=never", "--log-verbose=-", sanitize_url(target)]
    return run_command_safe(cmd, timeout=30)
