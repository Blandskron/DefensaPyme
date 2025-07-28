import re
from app.utils.shell import run_command_safe

def sanitize_url(target: str) -> str:
    return target.strip().split()[0] if target.startswith("http") else "http://" + target.strip().split()[0]

def detect_waf(target: str) -> str:
    cmd = ["wafw00f", sanitize_url(target)]
    output = run_command_safe(cmd)
    # Remueve códigos ANSI
    return re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', output)
