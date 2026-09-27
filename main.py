import os
from dotenv import load_dotenv
from src.ip_discovery import get_my_public_ip
from src.notifier import send_discord_alert
from src.reporter import print_exposure_report
from src.shodan_client import scan_ip_with_shodan

load_dotenv()


def main():
    shodan_key = os.getenv("SHODAN_API_KEY")
    discord_url = os.getenv("DISCORD_WEBHOOK_URL")

    print("Discovering public IP address...")
    public_ip = get_my_public_ip()

    if not public_ip:
        print("ERROR: Could not determine public IP address. Exiting.")
        return

    print(f"Scanning IP: {public_ip} via Shodan API...")
    scan_results = scan_ip_with_shodan(public_ip, shodan_key)

    # 1. Print report to terminal
    print_exposure_report(scan_results)

    # 2. Send webhook notification if Discord URL is present and not placeholder
    if discord_url and "YOUR/WEBHOOK/URL" not in discord_url:
        send_discord_alert(scan_results, discord_url)


if __name__ == "__main__":
    main()