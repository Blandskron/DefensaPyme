import re
import requests

def sanitize_url(target: str) -> str:
    if target.startswith("http"):
        return target.strip().split()[0]
    return "http://" + target.strip().split()[0]

def analyze_security_headers(target: str) -> dict:
    headers_expected = [
        "Strict-Transport-Security", "X-Content-Type-Options",
        "X-Frame-Options", "Content-Security-Policy", "Referrer-Policy"
    ]
    try:
        url = sanitize_url(target)
        response = requests.get(url, timeout=5)
        headers = response.headers
        return {
            key: ("" if key in headers else "Missing")
            for key in headers_expected
        }
    except Exception as e:
        return {"error": str(e)}
