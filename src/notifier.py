import requests


def send_discord_alert(data: dict, webhook_url: str):
    """Sends a formatted alert embed to a Discord channel via webhook."""
    status = data.get("status")
    ip_addr = data.get("ip_str") or data.get("ip") or "Unknown IP"

    if status == "CLEAN":
        embed = {
            "title": f"Network Status: CLEAN ({ip_addr})",
            "description": f"Shodan has no record of open ports or exposed services for `{ip_addr}`.",
            "color": 5763719,  # Green
            "footer": {"text": "Shodan Sentinel - Clean Scan"},
        }
    elif status == "ERROR":
        embed = {
            "title": "Shodan Sentinel Scan Error",
            "description": f"An error occurred while performing host lookup:\n```{data.get('message')}```",
            "color": 15548997,  # Red
        }
    else:
        open_ports = ", ".join(map(str, data.get("ports", [])))
        hostnames = ", ".join(data.get("hostnames", [])) or "None resolved"
        vulns = data.get("vulns", [])
        cve_text = ", ".join(vulns) if vulns else "None detected"

        embed = {
            "title": f"Shodan Exposure Alert: {ip_addr}",
            "color": 15548997,  # Red
            "fields": [
                {
                    "name": "Hostnames",
                    "value": hostnames,
                    "inline": False,
                },
                {
                    "name": "Open Ports Detected",
                    "value": f"`{open_ports}`" if open_ports else "None",
                    "inline": False,
                },
                {"name": "Known CVEs", "value": cve_text, "inline": False},
            ],
            "footer": {"text": "Shodan Sentinel - InternetDB Scan"},
        }

    payload = {"username": "Shodan Sentinel Bot", "embeds": [embed]}

    try:
        response = requests.post(webhook_url, json=payload, timeout=5)
        response.raise_for_status()
        print("Discord notification delivered successfully.")
    except requests.RequestException as e:
        print(f"ERROR: Failed to send Discord notification: {e}")