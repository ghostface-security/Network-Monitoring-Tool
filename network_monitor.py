from scapy.all import sniff
from collections import defaultdict
import datetime

active_connections = defaultdict(lambda: {"start_time": None, "end_time": None})

def packet_callback(packet):
    if "IP" in packet:
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        
        if "TCP" in packet:
            src_port = packet["TCP"].sport
            dst_port = packet["TCP"].dport
            protocol = "TCP"
        elif "UDP" in packet:
            src_port = packet["UDP"].sport
            dst_port = packet["UDP"].dport
            protocol = "UDP"
        else:
            return

        connection_key = tuple(sorted(((src_ip, src_port), (dst_ip, dst_port))))
        
        if active_connections[connection_key]["start_time"] is None:
            active_connections[connection_key]["start_time"] = datetime.datetime.now()
            print(f"[{active_connections[connection_key]['start_time']}] NEW CONNECTION: {protocol} {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
            
sniff(prn=packet_callback, store=0)
