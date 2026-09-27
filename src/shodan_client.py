import requests


def scan_ip_with_shodan(ip_address: str, api_key: str = None) -> dict:
    """Queries Shodan's free InternetDB REST endpoint for a given IP address."""
    url = f"https://internetdb.shodan.io/{ip_address}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            return {"status": "CLEAN", "ip": ip_address}

        response.raise_for_status()
        raw_data = response.json()

        return {
            "status": "EXPOSED",
            "ip_str": raw_data.get("ip"),
            "hostnames": raw_data.get("hostnames", []),
            "ports": raw_data.get("ports", []),
            "data": [
                {"port": p, "product": "Open Port", "version": ""}
                for p in raw_data.get("ports", [])
            ],
            "vulns": raw_data.get("vulns", []),
        }

    except Exception as err:
        return {"status": "ERROR", "message": str(err)}