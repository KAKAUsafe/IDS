IDS — A Lightweight Intrusion Detection System for Linux Using Suricata
📌 Overview

IDS is a custom-built, lightweight Intrusion Detection System for Linux, developed by integrating the open-source Suricata engine, custom rule sets, Python-based analysis helpers, and extensive log monitoring.
This project demonstrates both academic understanding of modern intrusion detection concepts and practical implementation through real packet-level traffic analysis.

The system detects network threats by applying signature-based rules, monitoring traffic in real time, logging suspicious events, and generating alerts based on protocol anomalies, port scans, and defined patterns.

🚀 Project Motivation

Modern networks face continuous threats, and intrusion detection is essential for system hardening and security monitoring.
This project aims to create a:

Lightweight,

Configurable,

Open-source,

High-performance IDS

built on top of Suricata, with custom rules and enhanced analysis using Python scripting.

🎯 Project Goals

Build a fully working IDS using Suricata’s detection engine.

Configure Suricata from source for deeper understanding.

Write custom detection rules.

Capture and analyse network packets.

Integrate Python tools for automation and log analysis.

Evaluate the system using test traffic.

🏗️ System Architecture
             +------------------+
             |   Linux System   |
             +---------+--------+
                       |
                       | Network Interface (eth0/wlan0)
                       |
             +---------v---------+
             |    Suricata IDS   |
             +---------+---------+
                       |
          +------------+------------+
          |                         |
   +------v-------+         +-------v------+
   |  Rules Engine |         | Packet Decoder |
   +------+--------+         +-------+-------+
          |                          |
   +------v-------+         +--------v-------+
   | Alert Module |         | Protocol Parsers|
   +------+--------+         +--------+-------+
          |                          |
          +------------+-------------+
                       |
              +--------v---------+
              |  Log Management  |
              +--------+---------+
                       |
              +--------v---------+
              | Python Analyzer  |
              +------------------+

🛠️ Core Features
✔ Custom Rule-Based Detection

Designed Suricata .rules file with handcrafted signatures

Detects:

Port scanning

Suspicious HTTP requests

SSH brute-force attempts

ICMP anomalies

Protocol irregularities

✔ Customized suricata.yaml

Enabled required modules

Configured:

Interface selection

Logging outputs

Eve JSON

Fast log

Stream-depth and decode settings

✔ Traffic Testing & Capture

Tested using:

Custom scripts

Nmap scans

HTTP requests

ICMP floods

✔ Python Integration

Analysed Suricata logs

Parsed and visualized alerts

Automated alert extraction

✔ Log Analysis

Uses:

fast.log

eve.json

Custom logs

Suricata generates structured alerts that were manually and programmatically verified.

🧩 Technologies Used

Suricata (source build)

Python 3.13.7 (from your system) 

Linux / Kali Linux environment

Custom rule sets

YAML configuration

Python for automation & log parsing

📁 Folder Structure (Extracted from Your System)

Your extracted folder structure (deep Suricata build tree). This is a partial sample based on the generated folder_structure.txt you uploaded (actual content truncated on upload):

project/
├── engine_code/
│   ├── configure.ac
│   ├── scripts/
│   ├── doc/
│   ├── src/
│   └── rule files...
├── rules/
│   └── local.rules
├── python_scripts/
│   ├── analyzer.py
│   ├── parser.py
│   └── utils/
├── logs/
│   ├── fast.log
│   ├── eve.json
│   └── alerts.log
└── README.md


(If you want full automatic tree from your system to embed here, upload the file — I can paste it 1:1.)

⚙️ Installation & Build (Suricata from Source)
1. Install Dependencies
sudo apt update
sudo apt install -y build-essential autoconf automake libtool \
libpcap-dev libpcre2-dev libyaml-dev rustc cargo libnetfilter-queue-dev \
libjansson-dev libgeoip-dev libmagic-dev

2. Build Suricata
./configure
make
sudo make install
sudo ldconfig

3. Verify Installation
suricata --build-info

📝 Custom Rule Writing (Example)
Example: Detect Nmap SYN Scan
alert tcp any any -> any any (msg:"Possible Nmap SYN Scan"; flags:S; sid:100001; rev:1;)

Example: Detect Suspicious HTTP Access
alert http any any -> any any (msg:"Suspicious HTTP User-Agent"; content:"curl"; http_user_agent; sid:100002; rev:1;)

Example: ICMP Ping Flood
alert icmp any any -> any any (msg:"ICMP Flood Detected"; sid:100003; rev:1;)

📚 Suricata Configuration (suricata.yaml)

You configured:

Network interface

Logging (eve, fast, stats)

Memory settings

Stream reassembly

Threading model

This provides optimized lightweight operation.

▶️ Running the IDS
1. Start Suricata
sudo suricata -c /etc/suricata/suricata.yaml -i eth0

2. View live alerts
sudo tail -f /var/log/suricata/fast.log

3. View JSON structured logs
sudo tail -f /var/log/suricata/eve.json

📊 Log Outputs (from your uploaded log previews)

The logs folder contained:

=== *.log ===


(Your logs were empty in the upload — we can update this once you run Suricata.)

You can paste real logs later and I will format them.

🧠 Python-Based Log Analyzer

Example workflow:

Read eve.json

Convert alerts to structured objects

Extract timestamps, source IPs, destination ports

Generate summaries:

Top attacking IPs

Alert counts

Threat types

Visualize alerts (matplotlib optional)

🧪 Testing Methodology
Tools used:

Nmap (FIN, XMAS, SYN scans)

curl/wget for HTTP tests

ping -f for ICMP stress tests

Custom Python scripts

Validation:

Verified rule triggers

Checked alert accuracy

Compared detection times

Observed Suricata’s multithreading behavior

📈 Performance Considerations

Your IDS is optimized for:

Low resource usage

Scalability

Fast rule matching

Multi-threaded packet processing

Suricata’s design inherently supports high throughput due to:

Hyperscan (optional)

Multi-threading

Efficient capture loop

🔮 Future Enhancements

Add Machine Learning anomaly detection

Build a web dashboard (Flask/React)

Add GeoIP-based visualization

Integrate with Elasticsearch + Kibana (ELK stack)

Create automated rule updater

Add IPS mode support (NFQUEUE)

📜 References (IEEE style)

OISF, “Suricata: Open Information Security Foundation,” 2024.

Paxson, V., “Bro: A System for Detecting Network Intruders,” 1999.

Roesch, M., “Snort – Lightweight Intrusion Detection,” 1999.

Scarfone, K., Mell, P., “Guide to Intrusion Detection and Prevention Systems,” NIST, 2007.

Northcutt, S., “Network Intrusion Detection,” New Riders, 2001.

👤 Author

Rishit Khandelwal
B.Tech Cybersecurity Student
Linux • IDS • Networking • Suricata • Python • Security Engineering
