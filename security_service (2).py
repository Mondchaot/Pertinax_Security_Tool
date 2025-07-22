import threading
from malware_scanner import scan_for_malware
from network_monitor import monitor_network
from threat_detector import detect_threats

def start_security_service():
    threading.Thread(target=scan_for_malware).start()
    threading.Thread(target=monitor_network).start()
    threading.Thread(target=detect_threats).start()