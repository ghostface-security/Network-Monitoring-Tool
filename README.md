💻 Network Monitoring Tool

Real-Time Network Connection Monitor
network_monitor.py is a lightweight Python script designed for real-time monitoring and logging of new network connections. Powered by the robust Scapy library, this tool passively sniffs network traffic and reports when new TCP or UDP connections are established on your system.

✨ Features

 * Real-Time Monitoring: Captures and analyzes network packets as they occur.
 * Connection Logging: Records new connections with a timestamp, protocol (TCP/UDP), source IP and port, and destination IP and port.
 * Protocol Support: Handles both TCP and UDP traffic.
 * Lightweight and Simple: A straightforward script that's easy to run and understand.
   
⚙️ How It Works

The script utilizes Scapy's sniff function to listen for all incoming and outgoing packets. Upon detecting a new packet, it verifies the presence of an IP layer followed by a TCP or UDP layer. A dictionary is used to track and store active connections. If the script identifies a new connection—defined by a unique source and destination IP/port pair—it logs the details to the console along with a timestamp.

🚀 Getting Started
Prerequisites

You'll need Python installed on your system. The primary dependency is the Scapy library, which you can install using pip:
pip install scapy

 * Note: You may need administrator or root privileges to capture network traffic, depending on your operating system.
Usage
Simply run the script from your terminal:
python network_monitor.py

The script will begin printing new connections to your console in real-time. To stop the monitor, press Ctrl+C.

⚠️ Disclaimer & Ethical Use

This tool is provided for educational purposes only and should be used exclusively on networks where you have explicit permission to monitor traffic.
 * Do not use this tool on networks you do not own or have authorization for.
 * Unauthorized network monitoring can be illegal and is a serious violation of privacy.
 * The author is not responsible for any misuse of this software. Always comply with local laws and regulations regarding network surveillance.
