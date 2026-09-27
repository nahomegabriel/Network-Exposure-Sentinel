# Network Exposure Sentinel

A modular Python security tool that discovers your public IP address, scans open ports and CVE vulnerabilities using Shodan's free InternetDB API, and delivers alerts directly to Discord via Webhooks.

## Features
- **Public IP Discovery:** Multi-endpoint fallback logic (ipify, ipinfo, icanhazip).
- **Exposure Scan:** Live check for open ports, hostnames, and CVEs without paid API keys.
- **Discord Alerting:** Automated embed notifications formatted cleanly without emojis.
- **Secret Protection:** `.env` secret isolation paired with `.gitignore` safeguards.

## Architecture
```text
.
├── .env.example       # Environment template
├── .gitignore          # Excludes secrets & virtualenvs
├── README.md           # Documentation
├── main.py             # Sentinel entry point
├── requirements.txt    # Project dependencies
└── src/
    ├── ip_discovery.py # Multi-endpoint IP resolver
    ├── notifier.py     # Discord Webhook integration
    ├── reporter.py     # Terminal output formatter
    └── shodan_client.py# Shodan InternetDB API client



Quickstart 

# Setup & Dependencies
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# Configure Secrets
cp .env.example .env && nano .env  # Add DISCORD_WEBHOOK_URL=[https://discord.com/](https://discord.com/)...

# Run Sentinel
python main.py