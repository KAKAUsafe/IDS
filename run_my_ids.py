import json
import time
import os
from datetime import datetime

# ---------------------------
# Color Codes
# ---------------------------
COLORS = {
    "RESET": "\033[0m",
    "LOW": "\033[92m",
    "MEDIUM": "\033[93m",
    "HIGH": "\033[91m",
    "CRITICAL": "\033[95m"
}

# ---------------------------
# Risk Classification Logic
# ---------------------------
def classify_risk(event):
    msg = event.get("alert", {}).get("signature", "").lower()
    ev = event.get("event_type", "")
    
    # ICMP / Ping
    if "icmp" in msg or ev == "icmp":
        return "LOW", "Normal ICMP / Ping"

    # Port Scans
    if "scan" in msg:
        return "MEDIUM", "Possible Port Scan"

    # DNS anomalies
    if ev == "dns":
        return "MEDIUM", "Suspicious DNS Activity"

    # HTTP anomalies
    if ev == "http":
        return "MEDIUM", "HTTP Suspicious Activity"

    # TLS/SSL
    if ev == "tls":
        return "HIGH", "TLS/SSL Irregular Activity"

    # SSH events
    if ev == "ssh":
        return "HIGH", "SSH Suspicious Login Activity"

    # Generic anomaly
    if ev == "anomaly":
        return "HIGH", "Protocol Anomaly"

    return "MEDIUM", "General Network Event"


# ---------------------------
# Follow eve.json Like Tail -f
# ---------------------------
def follow_file(path):
    with open(path, "r") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line


# ---------------------------
# MAIN FUNCTION
# ---------------------------
def main():
    LOGFILE = "/home/rishit/Desktop/IDS/logs/eve.json"

    print("\n-------------------------------------")
    print("   IDS Log Monitor - Real Time View   ")
    print("-------------------------------------\n")

    for line in follow_file(LOGFILE):
        try:
            event = json.loads(line)

            if "alert" not in event:
                continue

            risk, meaning = classify_risk(event)
            color = COLORS.get(risk, COLORS["RESET"])

            timestamp = event.get("timestamp", "N/A")
            sig = event["alert"].get("signature", "Unknown")
            src = event.get("src_ip", "?")
            dest = event.get("dest_ip", "?")

            print(f"{color}[{risk}] {meaning}{COLORS['RESET']}")
            print(f" → {timestamp} | {sig}")
            print(f"    {src}  →  {dest}\n")

        except Exception:
            continue


if __name__ == "__main__":
    main()

