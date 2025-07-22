import socket
import logging

def check_open_ports(host='localhost'):
    for port in range(20, 1024):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            if result == 0:
                logging.warning(f"Open port detected: {port}")
