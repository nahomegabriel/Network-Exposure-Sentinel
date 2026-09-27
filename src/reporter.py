def print_exposure_report(data: dict):
    """Formats and displays the Shodan scan results."""
    status = data.get("status")

    if status == "CLEAN":
        print("\n" + "=" * 50)
        print(f"SAFE: Shodan has no record of open ports for IP: {data.get('ip')}")
        print("Your network is not publicly indexed or exposed on Shodan.")
        print("=" * 50)
        return

    if status == "ERROR":
        print(f"ERROR: Scan failed: {data.get('message')}")
        return

    print("\n" + "=" * 50)
    print(f"SHODAN EXPOSURE REPORT FOR: {data.get('ip_str')}")
    print("=" * 50)

    hostnames = data.get("hostnames", [])
    if hostnames:
        print(f"\nHostnames: {', '.join(hostnames)}")

    open_ports = data.get("ports", [])
    print(f"\nOpen Ports Detected ({len(open_ports)}): {open_ports}")

    print("\nDetected Running Services:")
    for service in data.get("data", []):
        port = service.get("port")
        product = service.get("product", "Unknown Service")
        version = service.get("version", "")
        print(f"  - Port {port}: {product} {version}".strip())

    vulns = data.get("vulns", [])
    if vulns:
        print(f"\nPotential CVEs/Vulnerabilities Detected ({len(vulns)}):")
        for cve in vulns:
            print(f"  - {cve}")
    else:
        print("\nNo known vulnerabilities (CVEs) flagged on this host.")