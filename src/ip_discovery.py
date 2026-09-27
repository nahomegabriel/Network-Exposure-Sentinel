import requests


def get_my_public_ip() -> str:
    """Discovers current public IP address with fallbacks."""
    # List of reliable public IP endpoints
    endpoints = [
        ("https://api.ipify.org?format=json", "json"),
        ("https://ipinfo.io/json", "json"),
        ("https://icanhazip.com", "text"),
    ]

    for url, resp_type in endpoints:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            if resp_type == "json":
                # Strip leading/trailing whitespace before parsing
                data = response.json()
                return data.get("ip")
            else:
                # Plain text response
                return response.text.strip()

        except Exception:
            # If one service fails or returns invalid JSON, try the next one
            continue

    print("Error: All public IP discovery endpoints failed.")
    return None