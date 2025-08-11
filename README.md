Real-Time Network Connection Monitor
This Python script, network_monitor.py, is a simple tool for monitoring and logging new network connections on your system. Built with the powerful Scapy library, it passively sniffs network traffic and reports when a new TCP or UDP connection is established.
Features
 * Real-Time Monitoring: Captures and analyzes network packets as they happen.
 * Connection Logging: Reports a new connection with a timestamp, protocol (TCP/UDP), source IP and port, and destination IP and port.
 * Protocol Agnostic: Handles both TCP and UDP traffic.
 * Simple & Lightweight: A straightforward script that's easy to run and understand.
How It Works
The script uses Scapy's sniff function to listen for all incoming and outgoing packets. When it detects a new packet, it checks for an IP layer and then a TCP or UDP layer. It uses a dictionary to keep track of active connections. If it encounters a new connection—defined by a unique source and destination IP/port pair—it logs the details and a timestamp.
Getting Started
Prerequisites
You'll need to have Python installed, along with the Scapy library. You can install Scapy using pip:
pip install scapy

Note: Depending on your operating system, you may need to run this with administrator or root privileges to capture network traffic.
Usage
Simply run the script from your terminal:
python network_monitor.py

The script will start printing new connections to your console in real-time. To stop the monitor, just press Ctrl+C.
