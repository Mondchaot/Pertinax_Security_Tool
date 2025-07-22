from malware_scanner import scan_for_malware
from network_monitor import monitor_network

def detect_threats():
    print("[ThreatDetector] Starte Bedrohungsscan...")
    scan_for_malware()
    monitor_network()